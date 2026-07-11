#!/usr/bin/env python3
import os
import sys
import time
import csv
import subprocess
import shutil
from datetime import datetime, timezone
import requests

# List of 50 Bioconductor packages to analyze
PACKAGES = [
    "S4Vectors", "AnnotationDbi", "IRanges", "SummarizedExperiment", "GenomicRanges",
    "BiocGenerics", "Biostrings", "Biobase", "BiocParallel", "BSgenome",
    "limma", "SingleCellExperiment", "Seqinfo", "GenomicFeatures", "GenomeInfoDb",
    "rtracklayer", "Rsamtools", "oligoClasses", "oligo", "edgeR",
    "ExperimentHub", "AnnotationHub", "ComplexHeatmap", "DESeq2", "BiocFileCache",
    "graph", "DelayedArray", "GenomicAlignments", "biomaRt", "VariantAnnotation",
    "SpatialExperiment", "rhdf5", "MultiAssayExperiment", "MatrixGenerics", "affy",
    "qvalue", "flowCore", "BiocStyle", "preprocessCore", "HDF5Array",
    "XVector", "scater", "impute", "Rgraphviz", "GSEABase",
    "ggtree", "minfi", "sva", "clusterProfiler", "txdbmaker"
]

def get_github_token():
    """Retrieve GitHub token from environment variables or ~/.env file."""
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        return token
    
    # Check ~/.env
    env_path = os.path.expanduser("~/.env")
    if os.path.exists(env_path):
        try:
            with open(env_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if "=" in line:
                        k, v = line.split("=", 1)
                        if k.strip() in ("GITHUB_TOKEN", "GH_TOKEN"):
                            return v.strip().strip('"').strip("'")
        except Exception as e:
            print(f"Warning: Could not read ~/.env: {e}", file=sys.stderr)
            
    # Check .env in current directory
    if os.path.exists(".env"):
        try:
            with open(".env", "r") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if "=" in line:
                        k, v = line.split("=", 1)
                        if k.strip() in ("GITHUB_TOKEN", "GH_TOKEN"):
                            return v.strip().strip('"').strip("'")
        except Exception as e:
            print(f"Warning: Could not read .env: {e}", file=sys.stderr)
            
    return None

def make_request(url, headers, params=None, max_retries=3):
    """Perform HTTP GET request with retry logic and rate limit awareness."""
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, params=params, timeout=15)
            if response.status_code == 403 and "rate limit" in response.text.lower():
                reset_time = int(response.headers.get("X-RateLimit-Reset", time.time() + 60))
                sleep_duration = max(reset_time - int(time.time()), 10)
                print(f"Rate limit exceeded. Sleeping for {sleep_duration} seconds...", file=sys.stderr)
                time.sleep(sleep_duration)
                continue
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed (attempt {attempt+1}/{max_retries}): {e}", file=sys.stderr)
            time.sleep(2 ** attempt)
    return None

def find_repository(package, headers):
    """Find the GitHub repository for a package. Check Bioconductor org first, then search."""
    url = f"https://api.github.com/repos/Bioconductor/{package}"
    response = make_request(url, headers)
    if response and response.status_code == 200:
        return "Bioconductor", package
        
    url = f"https://api.github.com/repos/Bioconductor-mirror/{package}"
    response = make_request(url, headers)
    if response and response.status_code == 200:
        return "Bioconductor-mirror", package
        
    search_url = "https://api.github.com/search/repositories"
    params = {
        "q": f"{package} in:name language:R",
        "sort": "stars",
        "order": "desc"
    }
    response = make_request(search_url, headers, params)
    if response and response.status_code == 200:
        results = response.json()
        for item in results.get("items", []):
            if item["name"].lower() == package.lower():
                owner = item["owner"]["login"]
                repo = item["name"]
                print(f"Found fallback GitHub repository for {package}: {owner}/{repo}")
                return owner, repo
                
    return None, None

def get_open_prs_count(owner, repo, headers):
    """Get the count of open pull requests."""
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    params = {
        "state": "open",
        "per_page": 100
    }
    response = make_request(url, headers, params)
    if not response or response.status_code != 200:
        return 0
        
    prs = response.json()
    pr_count = len(prs)
    
    link_header = response.headers.get("Link")
    if link_header:
        parts = link_header.split(",")
        for part in parts:
            if 'rel="last"' in part:
                last_url = part.split(";")[0].strip("< >")
                try:
                    import urllib.parse as urlparse
                    parsed = urlparse.urlparse(last_url)
                    last_page = int(urlparse.parse_qs(parsed.query)["page"][0])
                    last_response = make_request(last_url, headers)
                    if last_response and last_response.status_code == 200:
                        pr_count = (last_page - 1) * 100 + len(last_response.json())
                        return pr_count
                except Exception:
                    pass
    return pr_count

def get_bioc_git_metrics(package, since_date, temp_parent_dir):
    """Clone repository from git.bioconductor.org and extract total and development commit metrics."""
    clone_dir = os.path.join(temp_parent_dir, f"clone_{package}")
    repo_url = f"https://git.bioconductor.org/packages/{package}.git"
    
    # Attempt shallow clone since since_date
    cmd_clone = [
        "git", "clone", 
        f"--shallow-since={since_date}", 
        "--single-branch", 
        repo_url, 
        clone_dir
    ]
    
    try:
        # Run clone with suppressed outputs
        result = subprocess.run(cmd_clone, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=45)
        
        # If shallow-since fails (e.g. no commits in range), try depth 1 clone
        if result.returncode != 0:
            shutil.rmtree(clone_dir, ignore_errors=True)
            cmd_clone_depth1 = [
                "git", "clone", 
                "--depth", "1", 
                "--single-branch", 
                repo_url, 
                clone_dir
            ]
            result = subprocess.run(cmd_clone_depth1, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=45)
            if result.returncode != 0:
                print(f"Error: Failed to clone {package} from git.bioconductor.org", file=sys.stderr)
                return None
                
        # Run git log to get the latest commit date (HEAD)
        cmd_last_commit = ["git", "log", "-1", "--format=%cI"]
        res_last = subprocess.run(cmd_last_commit, cwd=clone_dir, capture_output=True, text=True, check=True)
        last_commit_iso = res_last.stdout.strip()
        
        # Run git log to get all commits (date + subject) since since_date
        cmd_count = ["git", "log", f"--since={since_date}", "--format=%cI|%s"]
        res_count = subprocess.run(cmd_count, cwd=clone_dir, capture_output=True, text=True, check=True)
        
        total_commits = 0
        dev_commits = 0
        
        lines = [line.strip() for line in res_count.stdout.split("\n") if line.strip()]
        for line in lines:
            if "|" in line:
                date_str, message = line.split("|", 1)
                total_commits += 1
                
                # Filter out standard Bioconductor administrative commits
                msg_lower = message.lower()
                is_admin = False
                if "bump" in msg_lower and "version" in msg_lower:
                    is_admin = True
                elif "bump x.y.z" in msg_lower:
                    is_admin = True
                elif "creation of release_" in msg_lower:
                    is_admin = True
                    
                if not is_admin:
                    dev_commits += 1
        
        # Clean up directory
        shutil.rmtree(clone_dir, ignore_errors=True)
        
        last_commit_date_str = last_commit_iso[:10] if last_commit_iso else "N/A"
        return {
            "last_commit_date": last_commit_date_str,
            "commits_last_2_years": total_commits,
            "dev_commits_last_2_years": dev_commits,
            "last_commit_iso": last_commit_iso
        }
    except Exception as e:
        print(f"Exception processing git repo for {package}: {e}", file=sys.stderr)
        shutil.rmtree(clone_dir, ignore_errors=True)
        return None

def analyze_packages():
    # Setup headers and auth
    token = get_github_token()
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Bioconductor-Health-Analyzer"
    }
    if token:
        print("GitHub token loaded successfully.")
        headers["Authorization"] = f"token {token}"
    else:
        print("Warning: No GitHub token found. Unauthenticated requests will face strict rate limits.", file=sys.stderr)

    # 2 years ago from July 11, 2026 is July 11, 2024
    two_years_ago = "2024-07-11T00:00:00Z"
    now = datetime.now(timezone.utc)
    results = []

    # Ensure local directory structure exists
    os.makedirs("results", exist_ok=True)
    temp_parent_dir = os.path.abspath("results/temp_clones")
    os.makedirs(temp_parent_dir, exist_ok=True)

    print(f"Starting analysis of {len(PACKAGES)} Bioconductor packages...")
    for idx, package in enumerate(PACKAGES, 1):
        print(f"[{idx}/{len(PACKAGES)}] Processing package: {package}...")
        
        # Query canonical Git server (2-year window)
        git_metrics = get_bioc_git_metrics(package, two_years_ago, temp_parent_dir)
        
        # Respect GitHub API rate limits
        time.sleep(0.5)
        
        # Query GitHub API for community stats
        owner, repo = find_repository(package, headers)
        
        github_found = False
        repo_full_name = "N/A"
        stars = 0
        forks = 0
        open_issues_and_prs = 0
        open_prs = 0
        open_issues = 0
        
        if owner and repo:
            repo_full_name = f"{owner}/{repo}"
            repo_url = f"https://api.github.com/repos/{repo_full_name}"
            repo_resp = make_request(repo_url, headers)
            if repo_resp and repo_resp.status_code == 200:
                repo_data = repo_resp.json()
                github_found = True
                stars = repo_data.get("stargazers_count", 0)
                forks = repo_data.get("forks_count", 0)
                open_prs = get_open_prs_count(owner, repo, headers)
                open_issues_and_prs = repo_data.get("open_issues_count", 0)
                open_issues = max(0, open_issues_and_prs - open_prs)

        # Parse development stats
        if git_metrics:
            last_commit_date_str = git_metrics["last_commit_date"]
            commits_last_2_years = git_metrics["commits_last_2_years"]
            dev_commits_last_2_years = git_metrics["dev_commits_last_2_years"]
            last_commit_iso = git_metrics["last_commit_iso"]
            
            days_since_last_commit = -1
            if last_commit_iso:
                try:
                    last_commit_date = datetime.fromisoformat(last_commit_iso.replace("Z", "+00:00"))
                    days_since_last_commit = (now - last_commit_date).days
                except Exception as e:
                    print(f"Error parsing date {last_commit_iso}: {e}", file=sys.stderr)
                    try:
                        last_commit_date = datetime.strptime(last_commit_date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
                        days_since_last_commit = (now - last_commit_date).days
                    except Exception:
                        pass
        else:
            last_commit_date_str = "N/A"
            commits_last_2_years = 0
            dev_commits_last_2_years = 0
            days_since_last_commit = -1

        # Classify package health status based on canonical Git DEVELOPMENT commits (2 years)
        if days_since_last_commit == -1:
            status = "Unknown"
        elif days_since_last_commit > 730:
            status = "Inactive/Abandoned"
        elif dev_commits_last_2_years == 0:
            status = "Stale (Admin-Only)"
        elif days_since_last_commit <= 90 and dev_commits_last_2_years >= 5:
            status = "Active"
        elif days_since_last_commit <= 365:
            status = "Maintenance Mode"
        elif days_since_last_commit <= 730:
            status = "Stale"
        else:
            status = "Unknown"
            
        results.append({
            "package": package,
            "repo": repo_full_name,
            "found": github_found,
            "stars": stars,
            "forks": forks,
            "open_issues_and_prs": open_issues_and_prs,
            "open_prs": open_prs,
            "open_issues": open_issues,
            "commits_last_2_years": commits_last_2_years,
            "dev_commits_last_2_years": dev_commits_last_2_years,
            "last_commit_date": last_commit_date_str,
            "days_since_last_commit": days_since_last_commit,
            "status": status
        })
        
        print(f"Finished {package}: Stars={stars}, Commits(2yr)={commits_last_2_years}, DevCommits(2yr)={dev_commits_last_2_years}, Status={status}")

    # Remove temporary clone parent directory
    shutil.rmtree(temp_parent_dir, ignore_errors=True)
    
    # Save CSV
    csv_file = "results/bioc_health_data.csv"
    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "package", "repo", "found", "stars", "forks",
            "open_issues_and_prs", "open_prs", "open_issues",
            "commits_last_2_years", "dev_commits_last_2_years",
            "last_commit_date", "days_since_last_commit", "status"
        ])
        writer.writeheader()
        writer.writerows(results)
    print(f"CSV data saved to {csv_file}")

    # Generate Markdown Report (saved directly to README.md)
    generate_markdown_report(results, csv_file)

def generate_markdown_report(results, csv_filepath):
    """Generate a clean, professional README.md summarizing package health."""
    report_file = "README.md"
    
    total_packages = len(results)
    github_found_packages = sum(1 for r in results if r["found"])
    
    # Count statuses
    status_counts = {}
    for r in results:
        status_counts[r["status"]] = status_counts.get(r["status"], 0) + 1
        
    active_cnt = status_counts.get("Active", 0)
    maint_cnt = status_counts.get("Maintenance Mode", 0)
    stale_cnt = status_counts.get("Stale", 0)
    stale_admin_cnt = status_counts.get("Stale (Admin-Only)", 0)
    inactive_cnt = status_counts.get("Inactive/Abandoned", 0)
    unknown_cnt = status_counts.get("Unknown", 0)
    
    most_active = sorted(results, key=lambda r: r["dev_commits_last_2_years"], reverse=True)[:5]
    
    # Stars and issues can only be evaluated for packages resolved on GitHub
    github_results = [r for r in results if r["found"]]
    most_starred = sorted(github_results, key=lambda r: r["stars"], reverse=True)[:5]
    most_issues = sorted(github_results, key=lambda r: r["open_issues"], reverse=True)[:5]

    with open(report_file, "w") as f:
        f.write("# Bioconductor Package Volatility and Health Analysis Report\n\n")
        f.write(f"**Date of Analysis:** {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write(f"**Total Packages Analyzed:** {total_packages}\n\n")
        
        f.write("## Executive Summary\n\n")
        f.write("This repository contains a comprehensive volatility and health analysis of 50 core Bioconductor packages. ")
        f.write("To measure **real development activity**, this study pulls **canonical git history** directly from the official Bioconductor Git server (`git.bioconductor.org`) over a **two-year window** (since July 2024). ")
        f.write("Importantly, the script programmatically **filters out automatic administrative commits** (version bumps performed twice a year for releases) to calculate the true number of developer-initiated changes. ")
        f.write("Community metrics (stars, forks, and issues) are queried from GitHub when a corresponding repository exists.\n\n")
        
        f.write("### Repository Status Distribution\n\n")
        f.write("| Status | Count | Percentage | Description |\n")
        f.write("| :--- | :---: | :---: | :--- |\n")
        f.write(f"| **Active** | {active_cnt} | {active_cnt/total_packages*100:.1f}% | Last commit within 90 days AND has >= 5 real development commits in 2 years |\n")
        f.write(f"| **Maintenance Mode** | {maint_cnt} | {maint_cnt/total_packages*100:.1f}% | Last commit within 1 year, with low/stable developer commits (1-4 commits) |\n")
        f.write(f"| **Stale (Admin-Only)** | {stale_admin_cnt} | {stale_admin_cnt/total_packages*100:.1f}% | Last commit within 2 years, but has **0 real development commits** (only auto version bumps) |\n")
        if stale_cnt > 0:
            f.write(f"| **Stale** | {stale_cnt} | {stale_cnt/total_packages*100:.1f}% | Last commit between 1 and 2 years ago with some history |\n")
        f.write(f"| **Inactive/Abandoned** | {inactive_cnt} | {inactive_cnt/total_packages*100:.1f}% | No commits in over 2 years (missing even automated bumps) |\n")
        if unknown_cnt > 0:
            f.write(f"| **Unknown** | {unknown_cnt} | {unknown_cnt/total_packages*100:.1f}% | Failed to clone repository metrics |\n")
        f.write("\n")
        
        f.write("### Key Insights\n\n")
        f.write(f"- **Real Development Activity:** **{active_cnt} packages ({active_cnt/total_packages*100:.1f}%)** are under active, ongoing development with regular feature additions or bug fixes beyond administrative bumps.\n")
        f.write(f"- **Administrative-Only Stagnation:** **{stale_admin_cnt} packages ({stale_admin_cnt/total_packages*100:.1f}%)** represent stale libraries. Although they receive automatic version bumps twice a year, they have received **zero real developer commits** in the last two years.\n")
        f.write(f"- **Maintenance Mode Stability:** **{maint_cnt} packages ({maint_cnt/total_packages*100:.1f}%)** are in maintenance mode—stable packages receiving very minor patches (1-4 developer commits in 2 years) as issues arise.\n\n")
        
        # Top active
        f.write("## Top 5 Most Active Packages (Real Development Commits in Last 2 Years)\n\n")
        f.write("| Package | Dev Commits (2 Yrs) | Total Commits (2 Yrs) | Last Commit Date | Status |\n")
        f.write("| :--- | :---: | :---: | :--- | :--- |\n")
        for r in most_active:
            f.write(f"| **{r['package']}** | {r['dev_commits_last_2_years']} | {r['commits_last_2_years']} | {r['last_commit_date']} | {r['status']} |\n")
        f.write("\n")
        
        # Top starred
        f.write("## Top 5 Most Starred Packages (Community Interest on GitHub)\n\n")
        f.write("| Package | GitHub Repository | Stars | Forks | Status |\n")
        f.write("| :--- | :--- | :---: | :---: | :--- |\n")
        for r in most_starred:
            f.write(f"| **{r['package']}** | [{r['repo']}](https://github.com/{r['repo']}) | {r['stars']} | {r['forks']} | {r['status']} |\n")
        f.write("\n")

        # Top issues
        f.write("## Top 5 Packages by Open Issues Backlog (on GitHub)\n\n")
        f.write("| Package | GitHub Repository | Open Issues | Open PRs | Status |\n")
        f.write("| :--- | :--- | :---: | :---: | :--- |\n")
        for r in most_issues:
            f.write(f"| **{r['package']}** | [{r['repo']}](https://github.com/{r['repo']}) | {r['open_issues']} | {r['open_prs']} | {r['status']} |\n")
        f.write("\n")

        # Detailed breakdown
        f.write("## Detailed Package Statistics\n\n")
        f.write("A complete raw dataset is available in [bioc_health_data.csv](results/bioc_health_data.csv)\n\n")
        f.write("| Package | GitHub Repository | Stars | Dev Commits (2 Yr) | Total Commits (2 Yr) | Last Commit | Days Stale | Status |\n")
        f.write("| :--- | :--- | :---: | :---: | :---: | :--- | :---: | :--- |\n")
        
        sorted_results = sorted(results, key=lambda r: r["package"].lower())
        for r in sorted_results:
            repo_link = f"[{r['repo']}](https://github.com/{r['repo']})" if r["found"] else "N/A"
            days_str = str(r["days_since_last_commit"]) if r["days_since_last_commit"] != -1 else "N/A"
            f.write(f"| {r['package']} | {repo_link} | {r['stars']} | {r['dev_commits_last_2_years']} | {r['commits_last_2_years']} | {r['last_commit_date']} | {days_str} | {r['status']} |\n")
            
        f.write("\n---\n\n")
        f.write("## How to Reproduce or Expand this Work\n\n")
        f.write("1. **Setup Authentication**:\n")
        f.write("   - Copy `.env.example` to `.env` and fill in your `GITHUB_TOKEN` to avoid rate limits when querying GitHub.\n\n")
        f.write("2. **Run Analysis**:\n")
        f.write("   - To run on all 50 packages:\n")
        f.write("     ```bash\n")
        f.write("     python3 scripts/analyze_bioc_health.py\n")
        f.write("     ```\n")
        f.write("   - To run on specific packages:\n")
        f.write("     ```bash\n")
        f.write("     python3 scripts/analyze_bioc_health.py S4Vectors limma preprocessCore\n")
        f.write("     ```\n")
        
    print(f"README.md saved.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        PACKAGES = sys.argv[1:]
    analyze_packages()
