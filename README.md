


You need mongo, python  ,Flask, pandas, numpy installed

In order for the server to work you need to download the data first. You do this by the command 
```
python dataDownloader.py
```

You will need to create a file 'enviroment.py' with connection string in it.

The first time it will take a while since it will download the available data for the configured currencies since 01.01.2000

After that the the file for processing and calculating charts is ResponseBuilder.py

You can look at deb.py for simple usage.

If you want to run the server run main.py

