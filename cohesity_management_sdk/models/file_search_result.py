# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.ad_object_meta_data
import cohesity_management_sdk.models.email_meta_data
import cohesity_management_sdk.models.file_version
import cohesity_management_sdk.models.universal_id
import cohesity_management_sdk.models.protection_source

class FileSearchResult(object):

    """Implementation of the 'FileSearchResult' model.

    Specifies details about the found file or folder.

    Attributes:
        ad_object_meta_data (AdObjectMetaData): Specifies details about the AD
            objects.
        document_type (string): Specifies the inferred document type.
        email_meta_data (EmailMetaData): Specifies details about the emails
            and the folder containing emails.
        file_versions (list of FileVersion): Array of File Versions.
            Specifies the different snapshot versions of a file or folder that
            were captured at different times.
        filename (string): Specifies the name of the found file or folder.
        is_folder (bool): Specifies if the found item is a folder. If true,
            the found item is a folder.
        job_id (long|int): Specifies the Job id for the Protection Job that is
            currently associated with object that contains the backed up file
            or folder. If the file or folder was backed up on current Cohesity
            Cluster, this field contains the id for the Job that captured the
            object that contains the file or folder. If the file or folder was
            backed up on a Primary Cluster and replicated to this Cohesity
            Cluster, a new Inactive Job is created, the object that contains
            the file or folder is now associated with new Inactive Job, and
            this field contains the id of the new Inactive Job.
        job_uid (UniversalId): Specifies the universal id of the Protection
            Job that backed up the object that contains the file or folder.
        protection_source (ProtectionSource): Specifies a generic structure
            that represents a node in the Protection Source tree. Node details
            will depend on the environment of the Protection Source.
        registered_source_id (long|int): Specifies the id of the top-level
            registered source (such as a vCenter Server) where the source
            object that contains the the file or folder is stored.
        source_id (long|int): Specifies the source id of the object that
            contains the file or folder.
        mtype (TypeFileSearchResultEnum): Specifies the type of the file
            document such as KDirectory, kFile, etc.
        view_box_id (long|int): Specifies the id of the Domain (View Box)
            where the source object that contains the file or folder is
            stored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ad_object_meta_data":'adObjectMetaData',
        "document_type":'documentType',
        "email_meta_data":'emailMetaData',
        "file_versions":'fileVersions',
        "filename":'filename',
        "is_folder":'isFolder',
        "job_id":'jobId',
        "job_uid":'jobUid',
        "protection_source":'protectionSource',
        "registered_source_id":'registeredSourceId',
        "source_id":'sourceId',
        "mtype":'type',
        "view_box_id":'viewBoxId'
    }

    def __init__(self,
                 ad_object_meta_data=None,
                 document_type=None,
                 email_meta_data=None,
                 file_versions=None,
                 filename=None,
                 is_folder=None,
                 job_id=None,
                 job_uid=None,
                 protection_source=None,
                 registered_source_id=None,
                 source_id=None,
                 mtype=None,
                 view_box_id=None):
        """Constructor for the FileSearchResult class"""

        # Initialize members of the class
        self.ad_object_meta_data = ad_object_meta_data
        self.document_type = document_type
        self.email_meta_data = email_meta_data
        self.file_versions = file_versions
        self.filename = filename
        self.is_folder = is_folder
        self.job_id = job_id
        self.job_uid = job_uid
        self.protection_source = protection_source
        self.registered_source_id = registered_source_id
        self.source_id = source_id
        self.mtype = mtype
        self.view_box_id = view_box_id


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        ad_object_meta_data = cohesity_management_sdk.models.ad_object_meta_data.AdObjectMetaData.from_dictionary(dictionary.get('adObjectMetaData')) if dictionary.get('adObjectMetaData') else None
        document_type = dictionary.get('documentType')
        email_meta_data = cohesity_management_sdk.models.email_meta_data.EmailMetaData.from_dictionary(dictionary.get('emailMetaData')) if dictionary.get('emailMetaData') else None
        file_versions = None
        if dictionary.get('fileVersions') != None:
            file_versions = list()
            for structure in dictionary.get('fileVersions'):
                file_versions.append(cohesity_management_sdk.models.file_version.FileVersion.from_dictionary(structure))
        filename = dictionary.get('filename')
        is_folder = dictionary.get('isFolder')
        job_id = dictionary.get('jobId')
        job_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('jobUid')) if dictionary.get('jobUid') else None
        protection_source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('protectionSource')) if dictionary.get('protectionSource') else None
        registered_source_id = dictionary.get('registeredSourceId')
        source_id = dictionary.get('sourceId')
        mtype = dictionary.get('type')
        view_box_id = dictionary.get('viewBoxId')

        # Return an object of this model
        return cls(ad_object_meta_data,
                   document_type,
                   email_meta_data,
                   file_versions,
                   filename,
                   is_folder,
                   job_id,
                   job_uid,
                   protection_source,
                   registered_source_id,
                   source_id,
                   mtype,
                   view_box_id)


