import argparse

from green_web import get_logger_n_app
# import logging.config


def get_cl_arguments():
    parser = argparse.ArgumentParser(prog='run-server.py', description='Runs a development server', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # parser.add_argument('--environment', metavar='type', choices=['development', 'test', 'production'], default='development', help='the type of environment cofiguration to use. Defaults to all \'development\'')
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()


if __name__ == '__main__':
    # logger.info('>>>>> Using {} environment configuration <<<<<'.format(green_app.config['SERVER_NAME']))
    logger, app = get_logger_n_app(environment='development')
    logger.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=app.config['DEBUG'])
