from bot import spark_bot as run_bot


def lambda_handler(event, context):
    run_bot('test')


'''
Testing only, ignore



if __name__ == '__main__':
    run_bot('Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNTU2YWFmOTAtMGExYi0xMWU4LTgzZDYtN2JlMDUzODYyN2Fj')
'''
