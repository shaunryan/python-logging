# Python Native Logging Examples

Currently includes:
- Console Logging
- Custom SQL Server Logging Handler

See the `logging.yaml` definition. Sql server logging is fully configurable in the config file.
This config file can be packaged with the wheel if necessary. Also note the environment variable `LOGGINGDEMOHOME=./` in `.env`
This variable can be used to point an application at location where the logging file is stored. If this is not set it will default to `./`

Currently configured against an Azure SQL DB, though the connection string can be changed in the config file.

## To Do

Tech debt to sort out.
- password redaction


## Install

In bash:

```bash
python -m venv venv
source venv/scrips/activate

pip install -r dev_requirements.txt
pip install -r requirements.txt
pip install -e .
```

## Execute the demo

See `logging.yaml`. The configuration should be obvious.


Ensure SQL Server is available with the following table:
```
create table [ops].[application_log]
(
    [id] int IDENTITY(1,1) NOT NULL,
    [name] varchar(100) NOT NULL,
    [created_at] datetime NOT NULL,
    [module_function] varchar(500) NOT NULL,
    [level] varchar(500) NOT NULL,
    [message] varchar(500) NOT NULL,
    CONSTRAINT pk_ops_application_log_id PRIMARY KEY CLUSTERED (id)
)
```

Edit the connection string as required in `logging.yml`


Execute by either:

```
python -m loggingdemo
```

or for debuging and development run `demo.py` by hitting F5 in vscode. Note the `.vscode/launch.json` settings:

```
{
    "version": "0.2.0",
    "configurations": [
        
        {
            "name": "Python: Main",
            "type": "python",
            "request": "launch",
            "program": "demo.py",
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env"
        }
    ]
}
```
