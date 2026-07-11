# Bioconductor Package Volatility and Health Analysis Report

**Date of Analysis:** 2026-07-11
**Total Packages Analyzed:** 50

## Executive Summary

This repository contains a comprehensive volatility and health analysis of 50 core Bioconductor packages. Unlike traditional analyses that rely purely on GitHub mirrors (which are often outdated or incomplete), this study pulls **canonical git history** directly from the official Bioconductor Git server (`git.bioconductor.org`). Community metrics (stars, forks, and issues) are queried from GitHub when a corresponding repository exists.

### Repository Status Distribution

| Status | Count | Percentage | Description |
| :--- | :---: | :---: | :--- |
| **Active** | 40 | 80.0% | Last commit within 90 days and regular activity (>=5 commits/yr) |
| **Maintenance Mode** | 10 | 20.0% | Last commit within 1 year, but low commit activity or stable bug fixes |
| **Stale** | 0 | 0.0% | Last commit between 1 and 2 years ago |
| **Inactive/Abandoned** | 0 | 0.0% | No commits in over 2 years |

### Key Insights

- **Active Maintenance:** **50 packages (100.0%)** have received updates in the last year on the Bioconductor Git server, confirming a highly active core ecosystem.
- **GitHub Mirror Accuracy:** Checking `git.bioconductor.org` directly revealed that packages previously flagged as "inactive" or "missing" on GitHub (e.g. `limma`, `edgeR`, and `preprocessCore`) are actually **actively updated** with release bumps and regular patches on the canonical Bioconductor server.
- **Community Presence:** **47 of 50 packages (94.0%)** were resolved to public repositories on GitHub. These repositories host the community discussions (stars, forks, and issues) listed below.

## Top 5 Most Active Packages (Commits in Last Year on git.bioconductor.org)

| Package | Commits (Last 1 Yr) | Last Commit Date | Status |
| :--- | :---: | :--- | :--- |
| **rhdf5** | 201 | 2026-05-26 | Active |
| **biomaRt** | 178 | 2026-07-01 | Active |
| **clusterProfiler** | 67 | 2026-04-28 | Active |
| **ggtree** | 60 | 2026-04-28 | Active |
| **rtracklayer** | 37 | 2026-06-10 | Active |

## Top 5 Most Starred Packages (Community Interest on GitHub)

| Package | GitHub Repository | Stars | Forks | Status |
| :--- | :--- | :---: | :---: | :--- |
| **ComplexHeatmap** | [jokergoo/ComplexHeatmap](https://github.com/jokergoo/ComplexHeatmap) | 1520 | 249 | Active |
| **clusterProfiler** | [YuLab-SMU/clusterProfiler](https://github.com/YuLab-SMU/clusterProfiler) | 1214 | 268 | Active |
| **ggtree** | [YuLab-SMU/ggtree](https://github.com/YuLab-SMU/ggtree) | 928 | 183 | Active |
| **DESeq2** | [thelovelab/DESeq2](https://github.com/thelovelab/DESeq2) | 467 | 113 | Active |
| **qvalue** | [StoreyLab/qvalue](https://github.com/StoreyLab/qvalue) | 122 | 38 | Active |

## Top 5 Packages by Open Issues Backlog (on GitHub)

| Package | GitHub Repository | Open Issues | Open PRs | Status |
| :--- | :--- | :---: | :---: | :--- |
| **clusterProfiler** | [YuLab-SMU/clusterProfiler](https://github.com/YuLab-SMU/clusterProfiler) | 365 | 0 | Active |
| **ComplexHeatmap** | [jokergoo/ComplexHeatmap](https://github.com/jokergoo/ComplexHeatmap) | 228 | 4 | Active |
| **ggtree** | [YuLab-SMU/ggtree](https://github.com/YuLab-SMU/ggtree) | 194 | 1 | Active |
| **minfi** | [hansenlab/minfi](https://github.com/hansenlab/minfi) | 125 | 8 | Active |
| **biomaRt** | [Huber-group-EMBL/biomaRt](https://github.com/Huber-group-EMBL/biomaRt) | 41 | 1 | Active |

## Detailed Package Statistics

A complete raw dataset is available in [bioc_health_data.csv](results/bioc_health_data.csv)

| Package | GitHub Repository | Stars | Commits (1 Yr) | Last Commit | Days Stale | Status |
| :--- | :--- | :---: | :---: | :--- | :---: | :--- |
| affy | [Bioconductor/affy](https://github.com/Bioconductor/affy) | 0 | 4 | 2026-04-28 | 73 | Maintenance Mode |
| AnnotationDbi | [Bioconductor/AnnotationDbi](https://github.com/Bioconductor/AnnotationDbi) | 10 | 7 | 2026-04-28 | 73 | Active |
| AnnotationHub | [Bioconductor/AnnotationHub](https://github.com/Bioconductor/AnnotationHub) | 19 | 10 | 2026-06-30 | 10 | Active |
| Biobase | [Bioconductor/Biobase](https://github.com/Bioconductor/Biobase) | 9 | 6 | 2026-04-28 | 73 | Active |
| BiocFileCache | [Bioconductor/BiocFileCache](https://github.com/Bioconductor/BiocFileCache) | 14 | 10 | 2026-04-28 | 73 | Active |
| BiocGenerics | [Bioconductor/BiocGenerics](https://github.com/Bioconductor/BiocGenerics) | 13 | 25 | 2026-07-07 | 4 | Active |
| BiocParallel | [Bioconductor/BiocParallel](https://github.com/Bioconductor/BiocParallel) | 69 | 4 | 2026-04-28 | 73 | Maintenance Mode |
| BiocStyle | [Bioconductor/BiocStyle](https://github.com/Bioconductor/BiocStyle) | 15 | 6 | 2026-04-28 | 73 | Active |
| biomaRt | [Huber-group-EMBL/biomaRt](https://github.com/Huber-group-EMBL/biomaRt) | 50 | 178 | 2026-07-01 | 10 | Active |
| Biostrings | [Bioconductor/Biostrings](https://github.com/Bioconductor/Biostrings) | 68 | 25 | 2026-07-04 | 6 | Active |
| BSgenome | [Bioconductor/BSgenome](https://github.com/Bioconductor/BSgenome) | 9 | 9 | 2026-04-28 | 73 | Active |
| clusterProfiler | [YuLab-SMU/clusterProfiler](https://github.com/YuLab-SMU/clusterProfiler) | 1214 | 67 | 2026-04-28 | 73 | Active |
| ComplexHeatmap | [jokergoo/ComplexHeatmap](https://github.com/jokergoo/ComplexHeatmap) | 1520 | 6 | 2026-04-28 | 73 | Active |
| DelayedArray | [Bioconductor/DelayedArray](https://github.com/Bioconductor/DelayedArray) | 29 | 19 | 2026-05-26 | 45 | Active |
| DESeq2 | [thelovelab/DESeq2](https://github.com/thelovelab/DESeq2) | 467 | 31 | 2026-04-28 | 73 | Active |
| edgeR | [davidrequena/edgeR](https://github.com/davidrequena/edgeR) | 4 | 27 | 2026-06-27 | 14 | Active |
| ExperimentHub | [Bioconductor/ExperimentHub](https://github.com/Bioconductor/ExperimentHub) | 11 | 9 | 2026-06-15 | 25 | Active |
| flowCore | [RGLab/flowCore](https://github.com/RGLab/flowCore) | 60 | 13 | 2026-05-27 | 44 | Active |
| GenomeInfoDb | [Bioconductor/GenomeInfoDb](https://github.com/Bioconductor/GenomeInfoDb) | 35 | 15 | 2026-05-22 | 49 | Active |
| GenomicAlignments | [Bioconductor/GenomicAlignments](https://github.com/Bioconductor/GenomicAlignments) | 11 | 11 | 2026-07-07 | 3 | Active |
| GenomicFeatures | [Bioconductor/GenomicFeatures](https://github.com/Bioconductor/GenomicFeatures) | 27 | 12 | 2026-04-28 | 73 | Active |
| GenomicRanges | [Bioconductor/GenomicRanges](https://github.com/Bioconductor/GenomicRanges) | 47 | 20 | 2026-07-07 | 3 | Active |
| ggtree | [YuLab-SMU/ggtree](https://github.com/YuLab-SMU/ggtree) | 928 | 60 | 2026-04-28 | 73 | Active |
| graph | [Bioconductor/graph](https://github.com/Bioconductor/graph) | 6 | 7 | 2026-04-28 | 73 | Active |
| GSEABase | [Bioconductor/GSEABase](https://github.com/Bioconductor/GSEABase) | 6 | 8 | 2026-04-28 | 73 | Active |
| HDF5Array | [Bioconductor/HDF5Array](https://github.com/Bioconductor/HDF5Array) | 12 | 8 | 2026-04-28 | 73 | Active |
| impute | N/A | 0 | 4 | 2026-04-28 | 73 | Maintenance Mode |
| IRanges | [Bioconductor/IRanges](https://github.com/Bioconductor/IRanges) | 23 | 24 | 2026-07-01 | 9 | Active |
| limma | [cran/limma](https://github.com/cran/limma) | 13 | 19 | 2026-05-31 | 41 | Active |
| MatrixGenerics | [Bioconductor/MatrixGenerics](https://github.com/Bioconductor/MatrixGenerics) | 12 | 4 | 2026-04-28 | 73 | Maintenance Mode |
| minfi | [hansenlab/minfi](https://github.com/hansenlab/minfi) | 64 | 5 | 2026-05-25 | 46 | Active |
| MultiAssayExperiment | [waldronlab/MultiAssayExperiment](https://github.com/waldronlab/MultiAssayExperiment) | 76 | 36 | 2026-04-28 | 73 | Active |
| oligo | [benilton/oligo](https://github.com/benilton/oligo) | 3 | 4 | 2026-04-28 | 73 | Maintenance Mode |
| oligoClasses | [jmacdon/oligoClasses](https://github.com/jmacdon/oligoClasses) | 0 | 4 | 2026-04-28 | 73 | Maintenance Mode |
| preprocessCore | N/A | 0 | 4 | 2026-04-28 | 73 | Maintenance Mode |
| qvalue | [StoreyLab/qvalue](https://github.com/StoreyLab/qvalue) | 122 | 5 | 2026-04-28 | 73 | Active |
| Rgraphviz | [cran/Rgraphviz](https://github.com/cran/Rgraphviz) | 0 | 4 | 2026-04-28 | 73 | Maintenance Mode |
| rhdf5 | [Bioconductor/rhdf5](https://github.com/Bioconductor/rhdf5) | 0 | 201 | 2026-05-26 | 46 | Active |
| Rsamtools | [Bioconductor/Rsamtools](https://github.com/Bioconductor/Rsamtools) | 30 | 9 | 2026-04-28 | 73 | Active |
| rtracklayer | N/A | 0 | 37 | 2026-06-10 | 30 | Active |
| S4Vectors | [Bioconductor/S4Vectors](https://github.com/Bioconductor/S4Vectors) | 18 | 36 | 2026-07-06 | 4 | Active |
| scater | [alanocallaghan/scater](https://github.com/alanocallaghan/scater) | 95 | 18 | 2026-06-30 | 11 | Active |
| Seqinfo | [Bioconductor/Seqinfo](https://github.com/Bioconductor/Seqinfo) | 1 | 9 | 2026-04-28 | 73 | Active |
| SingleCellExperiment | [drisso/SingleCellExperiment](https://github.com/drisso/SingleCellExperiment) | 75 | 7 | 2026-05-14 | 58 | Active |
| SpatialExperiment | [drighelli/SpatialExperiment](https://github.com/drighelli/SpatialExperiment) | 74 | 4 | 2026-04-28 | 73 | Maintenance Mode |
| SummarizedExperiment | [Bioconductor/SummarizedExperiment](https://github.com/Bioconductor/SummarizedExperiment) | 38 | 8 | 2026-04-28 | 73 | Active |
| sva | [jtleek/sva](https://github.com/jtleek/sva) | 3 | 4 | 2026-04-28 | 73 | Maintenance Mode |
| txdbmaker | [Bioconductor/txdbmaker](https://github.com/Bioconductor/txdbmaker) | 5 | 12 | 2026-04-28 | 73 | Active |
| VariantAnnotation | [Bioconductor/VariantAnnotation](https://github.com/Bioconductor/VariantAnnotation) | 31 | 8 | 2026-04-28 | 73 | Active |
| XVector | [Bioconductor/XVector](https://github.com/Bioconductor/XVector) | 3 | 7 | 2026-04-28 | 73 | Active |

---

## How to Reproduce or Expand this Work

1. **Setup Authentication**:
   - Copy `.env.example` to `.env` and fill in your `GITHUB_TOKEN` to avoid rate limits when querying GitHub.

2. **Run Analysis**:
   - To run on all 50 packages:
     ```bash
     python3 scripts/analyze_bioc_health.py
     ```
   - To run on specific packages:
     ```bash
     python3 scripts/analyze_bioc_health.py S4Vectors limma preprocessCore
     ```
