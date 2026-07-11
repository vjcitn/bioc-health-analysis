# Bioconductor Package Volatility and Health Analysis Report

**Date of Analysis:** 2026-07-11
**Total Packages Analyzed:** 50

## Executive Summary

This report presents a comprehensive volatility and health analysis of 50 core Bioconductor packages. Repository metadata and commit histories were analyzed using the GitHub API to measure developer activity and community engagement over the last year.

### Repository Status Distribution

| Status | Count | Percentage | Description |
| :--- | :---: | :---: | :--- |
| **Active** | 33 | 66.0% | Last commit within 90 days and regular activity (>=5 commits/yr) |
| **Maintenance Mode** | 3 | 6.0% | Last commit within 1 year, but low commit activity or stable bug fixes |
| **Stale** | 2 | 4.0% | Last commit between 1 and 2 years ago |
| **Inactive/Abandoned** | 9 | 18.0% | No commits in over 2 years |
| **Not Found on GitHub** | 3 | 6.0% | Repository not found under Bioconductor organization or public search |

### Key Insights

- **Developer Activity:** 36 packages (72.0%) have received updates in the last year, indicating they are still actively maintained.
- **Deprecation / Stale Risks:** There are 11 packages (22.0%) that haven't received updates in over a year. These may represent stable codebases or potential maintenance risks.
- **Unmirrored/Private Code:** 3 packages could not be resolved on GitHub. These are likely maintained exclusively on `git.bioconductor.org` or in private repositories.

## Top 5 Most Active Packages (Commits in Last Year)

| Package | Repository | Commits (Last 1 Yr) | Last Commit Date | Status |
| :--- | :--- | :---: | :--- | :--- |
| **biomaRt** | [Huber-group-EMBL/biomaRt](https://github.com/Huber-group-EMBL/biomaRt) | 178 | 2026-07-01 | Active |
| **clusterProfiler** | [YuLab-SMU/clusterProfiler](https://github.com/YuLab-SMU/clusterProfiler) | 76 | 2026-07-09 | Active |
| **ggtree** | [YuLab-SMU/ggtree](https://github.com/YuLab-SMU/ggtree) | 65 | 2026-04-29 | Active |
| **MultiAssayExperiment** | [waldronlab/MultiAssayExperiment](https://github.com/waldronlab/MultiAssayExperiment) | 37 | 2026-04-29 | Active |
| **S4Vectors** | [Bioconductor/S4Vectors](https://github.com/Bioconductor/S4Vectors) | 36 | 2026-07-07 | Active |

## Top 5 Most Starred Packages (Community Interest)

| Package | Repository | Stars | Forks | Status |
| :--- | :--- | :---: | :---: | :--- |
| **ComplexHeatmap** | [jokergoo/ComplexHeatmap](https://github.com/jokergoo/ComplexHeatmap) | 1520 | 249 | Maintenance Mode |
| **clusterProfiler** | [YuLab-SMU/clusterProfiler](https://github.com/YuLab-SMU/clusterProfiler) | 1214 | 268 | Active |
| **ggtree** | [YuLab-SMU/ggtree](https://github.com/YuLab-SMU/ggtree) | 928 | 183 | Active |
| **DESeq2** | [thelovelab/DESeq2](https://github.com/thelovelab/DESeq2) | 467 | 113 | Maintenance Mode |
| **qvalue** | [StoreyLab/qvalue](https://github.com/StoreyLab/qvalue) | 122 | 38 | Inactive/Abandoned |

## Top 5 Packages by Open Issues Backlog

| Package | Repository | Open Issues | Open PRs | Status |
| :--- | :--- | :---: | :---: | :--- |
| **clusterProfiler** | [YuLab-SMU/clusterProfiler](https://github.com/YuLab-SMU/clusterProfiler) | 365 | 0 | Active |
| **ComplexHeatmap** | [jokergoo/ComplexHeatmap](https://github.com/jokergoo/ComplexHeatmap) | 228 | 4 | Maintenance Mode |
| **ggtree** | [YuLab-SMU/ggtree](https://github.com/YuLab-SMU/ggtree) | 194 | 1 | Active |
| **minfi** | [hansenlab/minfi](https://github.com/hansenlab/minfi) | 125 | 8 | Inactive/Abandoned |
| **biomaRt** | [Huber-group-EMBL/biomaRt](https://github.com/Huber-group-EMBL/biomaRt) | 41 | 1 | Active |

## Detailed Package Statistics

A complete raw dataset is available in [bioc_health_data.csv](file:///Users/vincentcarey/Documents/TestAntigravity/results/bioc_health_data.csv)

| Package | GitHub Repository | Stars | Commits (1 Yr) | Last Commit | Days Stale | Status |
| :--- | :--- | :---: | :---: | :--- | :---: | :--- |
| affy | [Bioconductor/affy](https://github.com/Bioconductor/affy) | 0 | 0 | 2023-07-12 | 1094 | Inactive/Abandoned |
| AnnotationDbi | [Bioconductor/AnnotationDbi](https://github.com/Bioconductor/AnnotationDbi) | 10 | 7 | 2026-04-28 | 73 | Active |
| AnnotationHub | [Bioconductor/AnnotationHub](https://github.com/Bioconductor/AnnotationHub) | 19 | 11 | 2026-06-30 | 10 | Active |
| Biobase | [Bioconductor/Biobase](https://github.com/Bioconductor/Biobase) | 9 | 6 | 2026-04-28 | 73 | Active |
| BiocFileCache | [Bioconductor/BiocFileCache](https://github.com/Bioconductor/BiocFileCache) | 14 | 11 | 2026-04-28 | 73 | Active |
| BiocGenerics | [Bioconductor/BiocGenerics](https://github.com/Bioconductor/BiocGenerics) | 13 | 25 | 2026-07-07 | 4 | Active |
| BiocParallel | [Bioconductor/BiocParallel](https://github.com/Bioconductor/BiocParallel) | 69 | 6 | 2026-04-29 | 72 | Active |
| BiocStyle | [Bioconductor/BiocStyle](https://github.com/Bioconductor/BiocStyle) | 15 | 6 | 2026-04-28 | 73 | Active |
| biomaRt | [Huber-group-EMBL/biomaRt](https://github.com/Huber-group-EMBL/biomaRt) | 50 | 178 | 2026-07-01 | 9 | Active |
| Biostrings | [Bioconductor/Biostrings](https://github.com/Bioconductor/Biostrings) | 68 | 25 | 2026-07-04 | 6 | Active |
| BSgenome | [Bioconductor/BSgenome](https://github.com/Bioconductor/BSgenome) | 9 | 9 | 2026-04-28 | 73 | Active |
| clusterProfiler | [YuLab-SMU/clusterProfiler](https://github.com/YuLab-SMU/clusterProfiler) | 1214 | 76 | 2026-07-09 | 2 | Active |
| ComplexHeatmap | [jokergoo/ComplexHeatmap](https://github.com/jokergoo/ComplexHeatmap) | 1520 | 3 | 2026-04-02 | 100 | Maintenance Mode |
| DelayedArray | [Bioconductor/DelayedArray](https://github.com/Bioconductor/DelayedArray) | 29 | 19 | 2026-05-26 | 45 | Active |
| DESeq2 | [thelovelab/DESeq2](https://github.com/thelovelab/DESeq2) | 467 | 29 | 2026-03-12 | 120 | Maintenance Mode |
| edgeR | [davidrequena/edgeR](https://github.com/davidrequena/edgeR) | 4 | 0 | 2018-02-06 | 3077 | Inactive/Abandoned |
| ExperimentHub | [Bioconductor/ExperimentHub](https://github.com/Bioconductor/ExperimentHub) | 11 | 10 | 2026-06-15 | 25 | Active |
| flowCore | [RGLab/flowCore](https://github.com/RGLab/flowCore) | 60 | 15 | 2026-05-27 | 44 | Active |
| GenomeInfoDb | [Bioconductor/GenomeInfoDb](https://github.com/Bioconductor/GenomeInfoDb) | 35 | 15 | 2026-05-22 | 49 | Active |
| GenomicAlignments | [Bioconductor/GenomicAlignments](https://github.com/Bioconductor/GenomicAlignments) | 11 | 11 | 2026-07-07 | 3 | Active |
| GenomicFeatures | [Bioconductor/GenomicFeatures](https://github.com/Bioconductor/GenomicFeatures) | 27 | 12 | 2026-04-28 | 73 | Active |
| GenomicRanges | [Bioconductor/GenomicRanges](https://github.com/Bioconductor/GenomicRanges) | 47 | 20 | 2026-07-07 | 3 | Active |
| ggtree | [YuLab-SMU/ggtree](https://github.com/YuLab-SMU/ggtree) | 928 | 65 | 2026-04-29 | 73 | Active |
| graph | [Bioconductor/graph](https://github.com/Bioconductor/graph) | 6 | 7 | 2026-04-28 | 73 | Active |
| GSEABase | [Bioconductor/GSEABase](https://github.com/Bioconductor/GSEABase) | 6 | 8 | 2026-04-28 | 73 | Active |
| HDF5Array | [Bioconductor/HDF5Array](https://github.com/Bioconductor/HDF5Array) | 12 | 8 | 2026-04-28 | 73 | Active |
| IRanges | [Bioconductor/IRanges](https://github.com/Bioconductor/IRanges) | 23 | 24 | 2026-07-01 | 9 | Active |
| limma | [cran/limma](https://github.com/cran/limma) | 13 | 0 | 2007-09-24 | 6865 | Inactive/Abandoned |
| MatrixGenerics | [Bioconductor/MatrixGenerics](https://github.com/Bioconductor/MatrixGenerics) | 12 | 4 | 2026-04-28 | 73 | Maintenance Mode |
| minfi | [hansenlab/minfi](https://github.com/hansenlab/minfi) | 64 | 0 | 2024-04-30 | 802 | Inactive/Abandoned |
| MultiAssayExperiment | [waldronlab/MultiAssayExperiment](https://github.com/waldronlab/MultiAssayExperiment) | 76 | 37 | 2026-04-29 | 72 | Active |
| oligo | [benilton/oligo](https://github.com/benilton/oligo) | 3 | 0 | 2025-03-08 | 489 | Stale |
| oligoClasses | [jmacdon/oligoClasses](https://github.com/jmacdon/oligoClasses) | 0 | 0 | 2020-08-10 | 2160 | Inactive/Abandoned |
| qvalue | [StoreyLab/qvalue](https://github.com/StoreyLab/qvalue) | 122 | 0 | 2023-09-01 | 1043 | Inactive/Abandoned |
| Rgraphviz | [cran/Rgraphviz](https://github.com/cran/Rgraphviz) | 0 | 0 | 2008-05-30 | 6616 | Inactive/Abandoned |
| rhdf5 | [Bioconductor/rhdf5](https://github.com/Bioconductor/rhdf5) | 0 | 0 | 2023-10-24 | 990 | Inactive/Abandoned |
| Rsamtools | [Bioconductor/Rsamtools](https://github.com/Bioconductor/Rsamtools) | 30 | 9 | 2026-04-28 | 73 | Active |
| S4Vectors | [Bioconductor/S4Vectors](https://github.com/Bioconductor/S4Vectors) | 18 | 36 | 2026-07-07 | 4 | Active |
| scater | [alanocallaghan/scater](https://github.com/alanocallaghan/scater) | 95 | 16 | 2026-04-29 | 73 | Active |
| Seqinfo | [Bioconductor/Seqinfo](https://github.com/Bioconductor/Seqinfo) | 1 | 9 | 2026-04-28 | 73 | Active |
| SingleCellExperiment | [drisso/SingleCellExperiment](https://github.com/drisso/SingleCellExperiment) | 75 | 7 | 2026-05-14 | 58 | Active |
| SpatialExperiment | [drighelli/SpatialExperiment](https://github.com/drighelli/SpatialExperiment) | 74 | 0 | 2025-05-08 | 428 | Stale |
| SummarizedExperiment | [Bioconductor/SummarizedExperiment](https://github.com/Bioconductor/SummarizedExperiment) | 38 | 8 | 2026-04-28 | 73 | Active |
| sva | [jtleek/sva](https://github.com/jtleek/sva) | 3 | 0 | 2015-10-13 | 3923 | Inactive/Abandoned |
| txdbmaker | [Bioconductor/txdbmaker](https://github.com/Bioconductor/txdbmaker) | 5 | 12 | 2026-04-28 | 73 | Active |
| VariantAnnotation | [Bioconductor/VariantAnnotation](https://github.com/Bioconductor/VariantAnnotation) | 31 | 8 | 2026-04-28 | 73 | Active |
| XVector | [Bioconductor/XVector](https://github.com/Bioconductor/XVector) | 3 | 7 | 2026-04-28 | 73 | Active |
| impute | N/A | 0 | 0 | N/A | N/A | Not Found |
| preprocessCore | N/A | 0 | 0 | N/A | N/A | Not Found |
| rtracklayer | N/A | 0 | 0 | N/A | N/A | Not Found |
