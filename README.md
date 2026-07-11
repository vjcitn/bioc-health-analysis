# Bioconductor Package Volatility and Health Analysis Report

**Date of Analysis:** 2026-07-11
**Total Packages Analyzed:** 50

## Executive Summary

This repository contains a comprehensive volatility and health analysis of 50 core Bioconductor packages. To measure **real development activity**, this study pulls **canonical git history** directly from the official Bioconductor Git server (`git.bioconductor.org`) over a **two-year window** (since July 2024). Importantly, the script programmatically **filters out automatic administrative commits** (version bumps performed twice a year for releases) to calculate the true number of developer-initiated changes. Community metrics (stars, forks, and issues) are queried from GitHub when a corresponding repository exists.

### Repository Status Distribution

| Status | Count | Percentage | Description |
| :--- | :---: | :---: | :--- |
| **Active** | 39 | 78.0% | Last commit within 90 days AND has >= 5 real development commits in 2 years |
| **Maintenance Mode** | 8 | 16.0% | Last commit within 1 year, with low/stable developer commits (1-4 commits) |
| **Stale (Admin-Only)** | 3 | 6.0% | Last commit within 2 years, but has **0 real development commits** (only auto version bumps) |
| **Inactive/Abandoned** | 0 | 0.0% | No commits in over 2 years (missing even automated bumps) |

### Key Insights

- **Real Development Activity:** **39 packages (78.0%)** are under active, ongoing development with regular feature additions or bug fixes beyond administrative bumps.
- **Administrative-Only Stagnation:** **3 packages (6.0%)** represent stale libraries. Although they receive automatic version bumps twice a year, they have received **zero real developer commits** in the last two years.
- **Maintenance Mode Stability:** **8 packages (16.0%)** are in maintenance mode—stable packages receiving very minor patches (1-4 developer commits in 2 years) as issues arise.

## Top 5 Most Active Packages (Real Development Commits in Last 2 Years)

| Package | Dev Commits (2 Yrs) | Total Commits (2 Yrs) | Last Commit Date | Status |
| :--- | :---: | :---: | :--- | :--- |
| **rhdf5** | 202 | 234 | 2026-05-26 | Active |
| **biomaRt** | 164 | 191 | 2026-07-01 | Active |
| **clusterProfiler** | 84 | 100 | 2026-04-28 | Active |
| **HDF5Array** | 76 | 84 | 2026-04-28 | Active |
| **ggtree** | 75 | 85 | 2026-04-28 | Active |

## Top 5 Most Starred Packages (Community Interest on GitHub)

| Package | GitHub Repository | Stars | Forks | Status |
| :--- | :--- | :---: | :---: | :--- |
| **ComplexHeatmap** | [jokergoo/ComplexHeatmap](https://github.com/jokergoo/ComplexHeatmap) | 1520 | 249 | Active |
| **clusterProfiler** | [YuLab-SMU/clusterProfiler](https://github.com/YuLab-SMU/clusterProfiler) | 1214 | 268 | Active |
| **ggtree** | [YuLab-SMU/ggtree](https://github.com/YuLab-SMU/ggtree) | 928 | 183 | Active |
| **DESeq2** | [thelovelab/DESeq2](https://github.com/thelovelab/DESeq2) | 467 | 113 | Active |
| **qvalue** | [StoreyLab/qvalue](https://github.com/StoreyLab/qvalue) | 122 | 38 | Maintenance Mode |

## Top 5 Packages by Open Issues Backlog (on GitHub)

| Package | GitHub Repository | Open Issues | Open PRs | Status |
| :--- | :--- | :---: | :---: | :--- |
| **clusterProfiler** | [YuLab-SMU/clusterProfiler](https://github.com/YuLab-SMU/clusterProfiler) | 365 | 0 | Active |
| **ComplexHeatmap** | [jokergoo/ComplexHeatmap](https://github.com/jokergoo/ComplexHeatmap) | 228 | 4 | Active |
| **ggtree** | [YuLab-SMU/ggtree](https://github.com/YuLab-SMU/ggtree) | 194 | 1 | Active |
| **minfi** | [hansenlab/minfi](https://github.com/hansenlab/minfi) | 125 | 8 | Maintenance Mode |
| **biomaRt** | [Huber-group-EMBL/biomaRt](https://github.com/Huber-group-EMBL/biomaRt) | 41 | 1 | Active |

## Detailed Package Statistics

A complete raw dataset is available in [bioc_health_data.csv](results/bioc_health_data.csv)

| Package | GitHub Repository | Stars | Dev Commits (2 Yr) | Total Commits (2 Yr) | Last Commit | Days Stale | Status |
| :--- | :--- | :---: | :---: | :---: | :--- | :---: | :--- |
| affy | [Bioconductor/affy](https://github.com/Bioconductor/affy) | 0 | 2 | 10 | 2026-04-28 | 73 | Maintenance Mode |
| AnnotationDbi | [Bioconductor/AnnotationDbi](https://github.com/Bioconductor/AnnotationDbi) | 10 | 4 | 12 | 2026-04-28 | 73 | Maintenance Mode |
| AnnotationHub | [Bioconductor/AnnotationHub](https://github.com/Bioconductor/AnnotationHub) | 19 | 29 | 42 | 2026-06-30 | 10 | Active |
| Biobase | [Bioconductor/Biobase](https://github.com/Bioconductor/Biobase) | 9 | 3 | 12 | 2026-04-28 | 73 | Maintenance Mode |
| BiocFileCache | [Bioconductor/BiocFileCache](https://github.com/Bioconductor/BiocFileCache) | 14 | 31 | 41 | 2026-04-28 | 73 | Active |
| BiocGenerics | [Bioconductor/BiocGenerics](https://github.com/Bioconductor/BiocGenerics) | 13 | 42 | 51 | 2026-07-07 | 4 | Active |
| BiocParallel | [Bioconductor/BiocParallel](https://github.com/Bioconductor/BiocParallel) | 69 | 21 | 36 | 2026-04-28 | 73 | Active |
| BiocStyle | [Bioconductor/BiocStyle](https://github.com/Bioconductor/BiocStyle) | 15 | 2 | 11 | 2026-04-28 | 73 | Maintenance Mode |
| biomaRt | [Huber-group-EMBL/biomaRt](https://github.com/Huber-group-EMBL/biomaRt) | 50 | 164 | 191 | 2026-07-01 | 10 | Active |
| Biostrings | [Bioconductor/Biostrings](https://github.com/Bioconductor/Biostrings) | 68 | 39 | 49 | 2026-07-04 | 6 | Active |
| BSgenome | [Bioconductor/BSgenome](https://github.com/Bioconductor/BSgenome) | 9 | 10 | 18 | 2026-04-28 | 73 | Active |
| clusterProfiler | [YuLab-SMU/clusterProfiler](https://github.com/YuLab-SMU/clusterProfiler) | 1214 | 84 | 100 | 2026-04-28 | 73 | Active |
| ComplexHeatmap | [jokergoo/ComplexHeatmap](https://github.com/jokergoo/ComplexHeatmap) | 1520 | 16 | 24 | 2026-04-28 | 73 | Active |
| DelayedArray | [Bioconductor/DelayedArray](https://github.com/Bioconductor/DelayedArray) | 29 | 35 | 43 | 2026-05-26 | 45 | Active |
| DESeq2 | [thelovelab/DESeq2](https://github.com/thelovelab/DESeq2) | 467 | 32 | 49 | 2026-04-28 | 73 | Active |
| edgeR | [davidrequena/edgeR](https://github.com/davidrequena/edgeR) | 4 | 63 | 73 | 2026-06-27 | 14 | Active |
| ExperimentHub | [Bioconductor/ExperimentHub](https://github.com/Bioconductor/ExperimentHub) | 11 | 19 | 31 | 2026-06-15 | 25 | Active |
| flowCore | [RGLab/flowCore](https://github.com/RGLab/flowCore) | 60 | 12 | 21 | 2026-05-27 | 44 | Active |
| GenomeInfoDb | [Bioconductor/GenomeInfoDb](https://github.com/Bioconductor/GenomeInfoDb) | 35 | 34 | 43 | 2026-05-22 | 49 | Active |
| GenomicAlignments | [Bioconductor/GenomicAlignments](https://github.com/Bioconductor/GenomicAlignments) | 11 | 10 | 18 | 2026-07-07 | 3 | Active |
| GenomicFeatures | [Bioconductor/GenomicFeatures](https://github.com/Bioconductor/GenomicFeatures) | 27 | 18 | 26 | 2026-04-28 | 73 | Active |
| GenomicRanges | [Bioconductor/GenomicRanges](https://github.com/Bioconductor/GenomicRanges) | 47 | 22 | 30 | 2026-07-07 | 3 | Active |
| ggtree | [YuLab-SMU/ggtree](https://github.com/YuLab-SMU/ggtree) | 928 | 75 | 85 | 2026-04-28 | 73 | Active |
| graph | [Bioconductor/graph](https://github.com/Bioconductor/graph) | 6 | 6 | 16 | 2026-04-28 | 73 | Active |
| GSEABase | [Bioconductor/GSEABase](https://github.com/Bioconductor/GSEABase) | 6 | 6 | 16 | 2026-04-28 | 73 | Active |
| HDF5Array | [Bioconductor/HDF5Array](https://github.com/Bioconductor/HDF5Array) | 12 | 76 | 84 | 2026-04-28 | 73 | Active |
| impute | N/A | 0 | 0 | 8 | 2026-04-28 | 73 | Stale (Admin-Only) |
| IRanges | [Bioconductor/IRanges](https://github.com/Bioconductor/IRanges) | 23 | 35 | 43 | 2026-07-01 | 9 | Active |
| limma | [cran/limma](https://github.com/cran/limma) | 13 | 46 | 55 | 2026-05-31 | 41 | Active |
| MatrixGenerics | [Bioconductor/MatrixGenerics](https://github.com/Bioconductor/MatrixGenerics) | 12 | 2 | 11 | 2026-04-28 | 73 | Maintenance Mode |
| minfi | [hansenlab/minfi](https://github.com/hansenlab/minfi) | 64 | 3 | 11 | 2026-05-25 | 46 | Maintenance Mode |
| MultiAssayExperiment | [waldronlab/MultiAssayExperiment](https://github.com/waldronlab/MultiAssayExperiment) | 76 | 70 | 103 | 2026-04-28 | 73 | Active |
| oligo | [benilton/oligo](https://github.com/benilton/oligo) | 3 | 7 | 15 | 2026-04-28 | 73 | Active |
| oligoClasses | [jmacdon/oligoClasses](https://github.com/jmacdon/oligoClasses) | 0 | 0 | 8 | 2026-04-28 | 73 | Stale (Admin-Only) |
| preprocessCore | N/A | 0 | 11 | 19 | 2026-04-28 | 73 | Active |
| qvalue | [StoreyLab/qvalue](https://github.com/StoreyLab/qvalue) | 122 | 1 | 9 | 2026-04-28 | 73 | Maintenance Mode |
| Rgraphviz | [cran/Rgraphviz](https://github.com/cran/Rgraphviz) | 0 | 25 | 34 | 2026-04-28 | 73 | Active |
| rhdf5 | [Bioconductor/rhdf5](https://github.com/Bioconductor/rhdf5) | 0 | 202 | 234 | 2026-05-26 | 46 | Active |
| Rsamtools | [Bioconductor/Rsamtools](https://github.com/Bioconductor/Rsamtools) | 30 | 9 | 17 | 2026-04-28 | 73 | Active |
| rtracklayer | N/A | 0 | 59 | 70 | 2026-06-10 | 30 | Active |
| S4Vectors | [Bioconductor/S4Vectors](https://github.com/Bioconductor/S4Vectors) | 18 | 35 | 47 | 2026-07-06 | 4 | Active |
| scater | [alanocallaghan/scater](https://github.com/alanocallaghan/scater) | 95 | 20 | 30 | 2026-06-30 | 11 | Active |
| Seqinfo | [Bioconductor/Seqinfo](https://github.com/Bioconductor/Seqinfo) | 1 | 12 | 16 | 2026-04-28 | 73 | Active |
| SingleCellExperiment | [drisso/SingleCellExperiment](https://github.com/drisso/SingleCellExperiment) | 75 | 5 | 14 | 2026-05-14 | 58 | Active |
| SpatialExperiment | [drighelli/SpatialExperiment](https://github.com/drighelli/SpatialExperiment) | 74 | 1 | 5 | 2026-04-28 | 73 | Maintenance Mode |
| SummarizedExperiment | [Bioconductor/SummarizedExperiment](https://github.com/Bioconductor/SummarizedExperiment) | 38 | 16 | 24 | 2026-04-28 | 73 | Active |
| sva | [jtleek/sva](https://github.com/jtleek/sva) | 3 | 0 | 8 | 2026-04-28 | 73 | Stale (Admin-Only) |
| txdbmaker | [Bioconductor/txdbmaker](https://github.com/Bioconductor/txdbmaker) | 5 | 19 | 28 | 2026-04-28 | 73 | Active |
| VariantAnnotation | [Bioconductor/VariantAnnotation](https://github.com/Bioconductor/VariantAnnotation) | 31 | 7 | 16 | 2026-04-28 | 73 | Active |
| XVector | [Bioconductor/XVector](https://github.com/Bioconductor/XVector) | 3 | 7 | 16 | 2026-04-28 | 73 | Active |

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
