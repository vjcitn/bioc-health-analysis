#!/usr/bin/env python3
import os
import sys
import time
import csv
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
    # Check direct environment variable
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
            
            # Check for rate limit
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
    # 1. Try Bioconductor organization
    url = f"https://api.github.com/repos/Bioconductor/{package}"
    response = make_request(url, headers)
    if response and response.status_code == 200:
        return "Bioconductor", package
        
    # 2. Try Bioconductor-mirror organization
    url = f"https://api.github.com/repos/Bioconductor-mirror/{package}"
    response = make_request(url, headers)
    if response and response.status_code == 200:
        return "Bioconductor-mirror", package
        
    # 3. Search GitHub for R repository with exact name
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
                print(f"Found fallback repository for {package}: {owner}/{repo}")
                return owner, repo
                
    return None, None

def get_commits_count_since(owner, repo, since_date, headers):
    """Count commits to default branch since since_date, handling pagination."""
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {
        "since": since_date,
        "per_page": 100
    }
    
    commit_count = 0
    page_url = url
    
    while page_url:
        response = make_request(page_url, headers, params if page_url == url else None)
        if not response or response.status_code != 200:
            break
            
        commits = response.json()
        commit_count += len(commits)
        
        # Check Link header for pagination
        link_header = response.headers.get("Link")
        next_url = None
        if link_header:
            parts = link_header.split(",")
            for part in parts:
                if 'rel="next"' in part:
                    next_url = part.split(";")[0].strip("< >")
                    break
        page_url = next_url
        
    return commit_count

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
    
    # Check if there are more pages (Link header)
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

    one_year_ago = "2025-07-11T00:00:00Z"
    now = datetime.now(timezone.utc)
    results = []

    print(f"Starting analysis of {len(PACKAGES)} Bioconductor packages...")
    for idx, package in enumerate(PACKAGES, 1):
        print(f"[{idx}/{len(PACKAGES)}] Processing package: {package}...")
        
        # Add delay to respect API rate limits
        time.sleep(0.5)
        
        owner, repo = find_repository(package, headers)
        
        if not owner or not repo:
            results.append({
                "package": package,
                "repo": "N/A",
                "found": False,
                "stars": 0,
                "forks": 0,
                "open_issues_and_prs": 0,
                "open_prs": 0,
                "open_issues": 0,
                "commits_last_year": 0,
                "last_commit_date": "N/A",
                "days_since_last_commit": -1,
                "status": "Not Found"
            })
            print(f"Repository not found for package: {package}")
            continue
            
        repo_full_name = f"{owner}/{repo}"
        
        # Fetch repository details
        repo_url = f"https://api.github.com/repos/{repo_full_name}"
        repo_resp = make_request(repo_url, headers)
        if not repo_resp or repo_resp.status_code != 200:
            print(f"Failed to fetch repository details for {repo_full_name}")
            continue
            
        repo_data = repo_resp.json()
        
        # Fetch last commit info
        commits_url = f"https://api.github.com/repos/{repo_full_name}/commits"
        commits_resp = make_request(commits_url, headers, params={"per_page": 1})
        
        last_commit_date_str = "N/A"
        days_since_last_commit = -1
        
        if commits_resp and commits_resp.status_code == 200:
            commits = commits_resp.json()
            if commits:
                commit_date_str = commits[0]["commit"]["committer"]["date"]
                try:
                    last_commit_date = datetime.strptime(commit_date_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
                    last_commit_date_str = last_commit_date.strftime("%Y-%m-%d")
                    days_since_last_commit = (now - last_commit_date).days
                except Exception as e:
                    print(f"Error parsing date {commit_date_str}: {e}", file=sys.stderr)

        # Count commits in the last 1 year
        commits_last_year = get_commits_count_since(owner, repo, one_year_ago, headers)
        
        # Count open Pull Requests
        open_prs = get_open_prs_count(owner, repo, headers)
        
        # Count open Issues (total open issues_and_prs contains both)
        open_issues_and_prs = repo_data.get("open_issues_count", 0)
        open_issues = max(0, open_issues_and_prs - open_prs)
        
        # Classify package status
        if days_since_last_commit == -1:
            status = "Unknown"
        elif days_since_last_commit <= 90:
            if commits_last_year >= 5:
                status = "Active"
            else:
                status = "Maintenance Mode"
        elif days_since_last_commit <= 365:
            status = "Maintenance Mode"
        elif days_since_last_commit <= 730:
            status = "Stale"
        else:
            status = "Inactive/Abandoned"
            
        results.append({
            "package": package,
            "repo": repo_full_name,
            "found": True,
            "stars": repo_data.get("stargazers_count", 0),
            "forks": repo_data.get("forks_count", 0),
            "open_issues_and_prs": open_issues_and_prs,
            "open_prs": open_prs,
            "open_issues": open_issues,
            "commits_last_year": commits_last_year,
            "last_commit_date": last_commit_date_str,
            "days_since_last_commit": days_since_last_commit,
            "status": status
        })
        
        print(f"Finished {package}: Stars={repo_data.get('stargazers_count', 0)}, Commits(1yr)={commits_last_year}, Status={status}")

    # Ensure output directories exist
    os.makedirs("results", exist_ok=True)
    
    # Save CSV
    csv_file = "results/bioc_health_data.csv"
    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "package", "repo", "found", "stars", "forks",
            "open_issues_and_prs", "open_prs", "open_issues",
            "commits_last_year", "last_commit_date", "days_since_last_commit", "status"
        ])
        writer.writeheader()
        writer.writerows(results)
    print(f"CSV data saved to {csv_file}")

    # Generate Markdown Report
    generate_markdown_report(results, csv_file)

def generate_markdown_report(results, csv_filepath):
    """Generate a clean, professional markdown report summarizing package health."""
    report_file = "results/bioc_health_report.md"
    
    total_packages = len(results)
    found_packages = sum(1 for r in results if r["found"])
    not_found_packages = total_packages - found_packages
    
    status_counts = {}
    for r in results:
        status_counts[r["status"]] = status_counts.get(r["status"], 0) + 1
        
    active_cnt = status_counts.get("Active", 0)
    maint_cnt = status_counts.get("Maintenance Mode", 0)
    stale_cnt = status_counts.get("Stale", 0)
    inactive_cnt = status_counts.get("Inactive/Abandoned", 0)
    not_found_cnt = status_counts.get("Not Found", 0)
    
    found_results = [r for r in results if r["found"]]
    most_active = sorted(found_results, key=lambda r: r["commits_last_year"], reverse=True)[:5]
    most_starred = sorted(found_results, key=lambda r: r["stars"], reverse=True)[:5]
    most_issues = sorted(found_results, key=lambda r: r["open_issues"], reverse=True)[:5]

    with open(report_file, "w") as f:
        f.write("# Bioconductor Package Volatility and Health Analysis Report\n\n")
        f.write(f"**Date of Analysis:** {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write(f"**Total Packages Analyzed:** {total_packages}\n\n")
        
        f.write("## Executive Summary\n\n")
        f.write("This report presents a comprehensive volatility and health analysis of 50 core Bioconductor packages. ")
        f.write("Repository metadata and commit histories were analyzed using the GitHub API to measure developer activity ")
        f.write("and community engagement over the last year.\n\n")
        
        f.write("### Repository Status Distribution\n\n")
        f.write("| Status | Count | Percentage | Description |\n")
        f.write("| :--- | :---: | :---: | :--- |\n")
        f.write(f"| **Active** | {active_cnt} | {active_cnt/total_packages*100:.1f}% | Last commit within 90 days and regular activity (>=5 commits/yr) |\n")
        f.write(f"| **Maintenance Mode** | {maint_cnt} | {maint_cnt/total_packages*100:.1f}% | Last commit within 1 year, but low commit activity or stable bug fixes |\n")
        f.write(f"| **Stale** | {stale_cnt} | {stale_cnt/total_packages*100:.1f}% | Last commit between 1 and 2 years ago |\n")
        f.write(f"| **Inactive/Abandoned** | {inactive_cnt} | {inactive_cnt/total_packages*100:.1f}% | No commits in over 2 years |\n")
        f.write(f"| **Not Found on GitHub** | {not_found_cnt} | {not_found_cnt/total_packages*100:.1f}% | Repository not found under Bioconductor organization or public search |\n\n")
        
        f.write("### Key Insights\n\n")
        f.write(f"- **Developer Activity:** {active_cnt + maint_cnt} packages ({ (active_cnt + maint_cnt)/total_packages*100:.1f}%) have received updates in the last year, indicating they are still actively maintained.\n")
        f.write(f"- **Deprecation / Stale Risks:** There are {stale_cnt + inactive_cnt} packages ({ (stale_cnt + inactive_cnt)/total_packages*100:.1f}%) that haven't received updates in over a year. These may represent stable codebases or potential maintenance risks.\n")
        f.write(f"- **Unmirrored/Private Code:** {not_found_packages} packages could not be resolved on GitHub. These are likely maintained exclusively on `git.bioconductor.org` or in private repositories.\n\n")
        
        f.write("## Top 5 Most Active Packages (Commits in Last Year)\n\n")
        f.write("| Package | Repository | Commits (Last 1 Yr) | Last Commit Date | Status |\n")
        f.write("| :--- | :--- | :---: | :--- | :--- |\n")
        for r in most_active:
            f.write(f"| **{r['package']}** | [{r['repo']}](https://github.com/{r['repo']}) | {r['commits_last_year']} | {r['last_commit_date']} | {r['status']} |\n")
        f.write("\n")
        
        f.write("## Top 5 Most Starred Packages (Community Interest)\n\n")
        f.write("| Package | Repository | Stars | Forks | Status |\n")
        f.write("| :--- | :--- | :---: | :---: | :--- |\n")
        for r in most_starred:
            f.write(f"| **{r['package']}** | [{r['repo']}](https://github.com/{r['repo']}) | {r['stars']} | {r['forks']} | {r['status']} |\n")
        f.write("\n")

        f.write("## Top 5 Packages by Open Issues Backlog\n\n")
        f.write("| Package | Repository | Open Issues | Open PRs | Status |\n")
        f.write("| :--- | :--- | :---: | :---: | :--- |\n")
        for r in most_issues:
            f.write(f"| **{r['package']}** | [{r['repo']}](https://github.com/{r['repo']}) | {r['open_issues']} | {r['open_prs']} | {r['status']} |\n")
        f.write("\n")

        f.write("## Detailed Package Statistics\n\n")
        f.write("A complete raw dataset is available in [bioc_health_data.csv](file://{})\n\n".format(os.path.abspath(csv_filepath)))
        f.write("| Package | GitHub Repository | Stars | Commits (1 Yr) | Last Commit | Days Stale | Status |\n")
        f.write("| :--- | :--- | :---: | :---: | :--- | :---: | :--- |\n")
        
        sorted_results = sorted(results, key=lambda r: (r["status"] == "Not Found", r["package"].lower()))
        for r in sorted_results:
            repo_link = f"[{r['repo']}](https://github.com/{r['repo']})" if r["found"] else "N/A"
            days_str = str(r["days_since_last_commit"]) if r["days_since_last_commit"] != -1 else "N/A"
            f.write(f"| {r['package']} | {repo_link} | {r['stars']} | {r['commits_last_year']} | {r['last_commit_date']} | {days_str} | {r['status']} |\n")
            
    print(f"Markdown report saved to {report_file}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        PACKAGES = sys.argv[1:]
    analyze_packages()
