<div align="center">
  <h1> ElasticSearch with Django </h1>
  <img src="https://cdn-media-1.freecodecamp.org/images/1*ojvTsI-Asv1IIjdm61RzKw.jpeg" width="400" title="elastic-search-django">
</div>

Sample django project using elastic search. This is quite simple but more detailed. I hope it will be super helpful for you if you are a beginner at elastic search.

### Elasticsearch

Elasticsearch is a distributed, free and open search and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured. It supports RESTful operations. It is one of the most popular search engines powering applications that have complex search requirements such as big e-commerce stores and analytic applications. It allows you to store, search, and analyze huge volumes of data quickly and in near real-time and give back answers in milliseconds. It's able to achieve fast search responses because instead of searching the text directly, it searches an index. (source: google)

**Django** is a Python-based free and open-source web framework.

# Pre-requisite & Guidelines

### 1.1 | download and install elasticsearch

Elasticsearch is a Java application, so the first step is to [install Java](https://www.oracle.com/java/technologies/javase-downloads.html). 

To install on debian:

```
$ sudo apt install default-jdk
```

To verify java installation, `$ java -version`. Output should be something like this:
```
openjdk version "11.0.11" 2021-04-20
OpenJDK Runtime Environment (build 11.0.11+9-Ubuntu-0ubuntu2.18.04)
OpenJDK 64-Bit Server VM (build 11.0.11+9-Ubuntu-0ubuntu2.18.04, mixed mode, sharing)
```

After getting java installed, [download](https://www.elastic.co/downloads/elasticsearch) **elasticsearch** [from here](https://www.elastic.co/downloads/elasticsearch).

To download on debian, use the following command,
```
# install elastic search APT repository, it should print OK.
$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

# add elastic search repo to the system
$ sudo sh -c 'echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" > /etc/apt/sources.list.d/elastic-7.x.list'
```

If you fail to download by using command line, just download `.deb` file [from here](https://www.elastic.co/downloads/elasticsearch) and install that using `ubuntu software`.

When the download is successfully completed, install elastic search on debian, use the following command,
```
# update packages index and install elastic search engine
$ sudo apt update
$ sudo apt install elasticsearch

# start and enable the service
$ sudo systemctl enable elasticsearch.service --now
```

To verify elastic search is running, use `$ curl -X GET "localhost:9200/"` or `$ curl http://localhost:9200/`.

Or, just open your browser and type [http://localhost:9200/](http://localhost:9200/).

Output should be something like this:
```
{
  "name" : "shiningflash007",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "5tOKVnMESmmEd15KPuNP-g",
  "version" : {
    "number" : "7.13.4",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "c5f60e894ca0c61cdbae4f5a686d9f08bcefc9123",
    "build_date" : "2021-07-14T18:33:36.673943207Z",
    "build_snapshot" : false,
    "lucene_version" : "8.8.2",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

**config**: Elasticsearch data is stored in the `/var/lib/elasticsearch` directory. Configuration files are located in `/etc/elasticsearch` and Java start-up options can be configured in the `/etc/default/elasticsearch` file.

Great!! So, now I hope you are successfully installed with both java and elastic search on your machine. Now, let's dig deeper...

### 1.2 | install django

We're using django here. I hope django is already installed on your machine. If not, then use `$ pip3 install Django` to install django. Make sure that you're installed with `Python` and `pip3` already. You can install python and pip3 using following commands,
```
$ sudo apt-get update
$ sudo apt-get install python3 
$ sudo apt-get install python3-pip
$ pip3 install Django
```

To verify django installation, use `$ django-admin –version`.

### 1.3 | create and set-up django application

```
$ django-admin startproject elastic
$ cd elastic
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
$ python3 manage.py runserver

# create an app and add it to the settings.py
$ python3 manage.py startapp user
```

I hope you're familiar with this command.

Now, your django application is also up and running. And you're fully ready, yayy!!

### 1.4 | install supporting libraries

All required libraries are listed in `requirements.txt` file. To install them together, `$ pip3 install -r requirements.txt`. Then, add them in the `settings.py` > INSTALLED_APP (`rest_framework`, `django_elasticsearch_dsl`, `django_elasticsearch_dsl_drf`). Also, add this below `INSTALLED_APP`,
```
ELASTICSEARCH_DSL = {
    'default': {
        'host': 'localhost:9200'
    }
}
```

# Run Project

1. Firstly, Create a virtualenv and activate that using `$ virtualenv venv` and `$ source venv/bin/activate`.
2. Then, install all necessary packages using `$ pip3 install -r requirements.txt`.
3. After that, migrate models using `$ python3 manage.py makemigrations migrate`.
4. Create index using `$ python3 manage.py search_index --rebuild`. <br>
To check the index mapping, `$ localhost:9200/<PUBLISHER_INDEX_NAME>`. (Note: In our case, PUBLISHER_INDEX is `elastic_demo`)
5. Finally, run the django project using `$ python3 manage.py runserver`.

Yayyy! You're all done. Now open your browser, search and enjoy elasticsearch...

Some example:
1. [http://localhost:8000/search/?search=club](http://localhost:8000/search/?search=club)
2. [http://localhost:8000/search/?color__contains=red](http://localhost:8000/search/?color__contains=red)
3. [http://localhost:8000/search/?info__contains=sister](http://localhost:8000/search/?info__contains=sister)

Congratulations... 🎉🎉

---

### Disclaimer

This is my first project in ElasticSearch. So, there are lots of things to improve. Feel free to create issues for improvement. Thanks in advance.