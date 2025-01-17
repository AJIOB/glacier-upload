from setuptools import setup, find_packages

setup(
    name="glacier_upload",
    version="1.2",
    description="AWS Glacier upload utility",
    # The project's main homepage.
    url="https://github.com/tbumi/glacier-upload",
    # Author details
    author="Trapsilo Bumi",
    author_email="tbumi@thpd.io",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="AWS Glacier upload multipart",
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=["docs", "tests"]),
    install_requires=["click", "boto3"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "glacier_upload=glacier_upload.upload:upload_command",
            "list_all_glacier_uploads=glacier_upload.list_uploads:list_all_uploads_command",
            "list_parts_in_upload=glacier_upload.list_uploads:list_parts_in_upload_command",
            "init_archive_retrieval=glacier_upload.initiate_job:init_archive_retrieval_command",
            "init_inventory_retrieval=glacier_upload.initiate_job:init_inventory_retrieval_command",
            "get_glacier_job_output=glacier_upload.get_job_output:get_job_output_command",
            "abort_glacier_upload=glacier_upload.manual_abort_upload:abort_upload_command",
            "delete_glacier_archive=glacier_upload.delete_archive:delete_archive_command",
        ]
    },
)
