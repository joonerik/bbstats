import os
from boto.s3.connection import S3Connection

def testDrit():
    s3 = S3Connection(os.environ['MONGODB_URI'])
    return s3
