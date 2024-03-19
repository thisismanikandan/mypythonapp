from apminsight import initialize_agent
initialize_agent({

        "appname" : "myfirstapp",

 

        '''change if  S247DataExporter is not running in the default ports(20021, 20022):'''

        "exporter_status_port" : "<S247DataExporter status port>",

        "exporter_data_port" : "<S247DataExporter data port>",

 

        '''If you are running S247DataExporter on a separate machine/server or as a Docker container:'''

        "exporter_host" : "<HostName/ContainerName where S247DataExporter is running>"
})

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)