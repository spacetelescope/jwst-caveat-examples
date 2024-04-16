# JWST Pipeline Caveat Notebooks

The repository contains notebooks or scripts intended to aid the community in mitigating issues that affect, or recently affected, data products available in the MAST archive.

Please direct all questions and comments about the information contained within to the [JWST Help Desk](https://jwsthelp.stsci.edu).

If you have a specific issue using one of the example scripts or notebooks, you can include a link to that file with the help desk call. 


Some issues can be fixed by reprocessing data on your computer, using the latest [JWST pipeline](https://github.com/spacetelescope/jwst) release and/or [calibration reference data](https://jwst-crds.stsci.edu/)(CRDS) context. 

It takes a few weeks to integrate a new calibration pipeline build into a full Science & Operations Center (S&OC) software build, test the S&OC build, fix subsystem interface issues, and finally install the S&OC build in operations. After that, fixes in the new pipeline software and/or reference data will be reflected in new (or replaced) products in MAST. 

[The software vs DMS build table in the JWST pipeline repository](https://github.com/spacetelescope/jwst) indicates when jwst builds were released, which reference data (CRDS) context they were tested with, and when the was first used in S&OC operations. Some JWST releases (particularly S&OC release candidates) are never installed in operations. That page also provides detailed instructions on how to create a fresh conda environment, install the version of the pipeline you would like to use, and how to configure the CRDS environment that is appropriate for that release.


## Deprecation of Notebooks

Once JWST DMS infrastructure has been updated, and the workarounds in a specific notebook are no longer neccessary or recommended, then the notebook will be deprecated. The process for deprecating a notebook includes the following:

*  Determine what calibration software version and CRDS context mitigated the issue worked around in the notebook
*  Determine the DATE when DMS operations first began generating data products that no longer require the workaround described in the notebook
*  Insert a new cell at the top of the notebook with a deprecation comment in a large font. The default deprecation comment is the following:


>This notebook is deprecated. Data products generated with calibration software version x.y.z or later, and CRDS context jwst_xxxx.pmap or later, no longer require this workaround. Data products in MAST created after DATE no longer require this workaround. To check creation dates for files in MAST, substitute your program ID for 2288 at the end of this URL:
>
>https://mast.stsci.edu/search/ui/#/jwst/results?select_cols=fileSetName,dataset,cal_ver,crds_ctx,date&program_id=2288


*  Submit a PR that includes the updated files
*  Make sure that the JDOX Known Issues table entry has been updated appropriately
*  Make sure that any related calibration pipeline documentation has been updated
*  After all affected products in MAST have been reprocessed, or after 3 months, whichever is 
longer, submit a PR that removes the notebook from the repository
*  Review any files being deprecated to assess whether an updated copy of the notebook should be submitted to the JDAT (https://github.com/spacetelescope/jdat_notebooks)  or JWST-PIPELINE-NOTEBOOKS (https://github.com/spacetelescope/jwst-pipeline-notebooks)  repository for long term use and maintenance.


