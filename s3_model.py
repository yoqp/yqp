# -*- coding: utf-8 -*-
from marshmallow import Schema, fields, post_load


class OwnerSchema(Schema):
    DisplayName = fields.Str()
    ID = fields.Str()


class ContentSchema(Schema):
    ETag = fields.Str()
    Key = fields.Str()
    LastModified = fields.Raw()
    Owner = fields.Nested(OwnerSchema)
    Size = fields.Integer()
    StorageClass = fields.Str()


class ResponseMetadataSchema(Schema):
    HTTPHeaders = fields.Raw()
    HTTPStatusCode = fields.Integer()
    HostId = fields.Str()
    RequestId = fields.Str()
    RetryAttempts = fields.Integer()


class S3(object):
    def __init__(self, Contents, EncodingType, IsTruncated, Marker, MaxKeys, Name, Prefix, ResponseMetadata):
        self.contents = Contents
        self.encoding_type = EncodingType
        self.is_truncated = IsTruncated
        self.marker = Marker
        self.max_keys = MaxKeys
        self.name = Name
        self.prefix = Prefix
        self.response_metadata = ResponseMetadata

    def __repr__(self):
        return '<S3(name={self.name!r})>'.format(self=self)

    def is_requirements(self, ts, id, version):
        # 必要なデータ
        requirements = ['file1.csv', file2.csv]

        file_names = []
        for t in ts:
            if file_names is None:
                file_names = [x.format(t=t) for x in reporting_requirement]
            else:
                file_names.extend([x.format(t=t) for x in requirements])
        files_on_s3 = [x['Key'].replace(f'reports/{id}/rev{version}/', '') for x in self.contents if len(x) > 0]
        if len(set(file_names) - set(files_on_s3)) > 0:
            return False
        return True


class S3Schema(Schema):
    Contents = fields.Nested(ContentSchema, many=True)
    EncodingType = fields.Str()
    IsTruncated = fields.Boolean()
    Marker = fields.Str()
    MaxKeys = fields.Integer()
    Name = fields.Str()
    Prefix = fields.Str()
    ResponseMetadata = fields.Nested(ResponseMetadataSchema)


    @post_load
    def make_s3(self, data):
        if 'Contents' in data:
            return S3(**data)
        return None 
