import boto3


def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    source_bucket = s3.Bucket('myworddocs')
    objects_in_source_bucket = source_bucket.objects.all()

    target_bucket = s3.Bucket('targetpdfbucket')

    for obj_file in objects_in_source_bucket:
        # download them and store in lambda /tmp directory
        source_bucket.download_file(obj_file.key, f'/tmp/{obj_file.key}')

        # Using 'convertapi'. This is a pay service. #Or, use any other service
        # So, not fully implemented
        # result = convertapi.convert('pdf', {'File': '/path/to/my_file.docx'})
        # result.file.save('/path/to/save/file.pdf')

        # Assuming the file is converted, next save it to the target bucket
        # make sure to change target file name in the below parameter
        # here iam using the same file name as the source
        target_bucket.put_object(Body=f'/tmp/{obj_file.key}', Key=f'{obj_file.key}')
