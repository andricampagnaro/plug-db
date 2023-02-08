class Connection:
    def create_url(self, drivername=None, host=None, port=None, username=None, password=None, database=None):
        logger.debug('Criar URL | Iniciando')
        url =  URL(drivername=drivername, 
                        username=username, 
                        password=password, 
                        host=host, 
                        port=port, 
                        database=database)
        return url
        logger.debug('Criar URL | Finalizado')

    def create_url_odbc(self, drivername=None, host=None, port=None, username=None, password=None, database=None):
        logger.debug('Criar URL | Iniciando')
        parametros = (
            f'DRIVER={driver};'
            f'SERVER={host};'
            f'PORT={port};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password}'
        )
        url = f'{drivername}+pyodbc:///?odbc_connect={quote_plus(parametros)}'
        return url
        logger.debug('Criar URL | Finalizado')

    def connect(self, url):
        logger.debug('Conectar banco | Iniciando')
        try:
            return create_engine(self.url)
            logger.debug('Conectar banco | Finalizado')
        except Exception as e:
            return e
            logger.error('Conectar banco | Error')

    def validation_method(self):
        return 'Class created!'