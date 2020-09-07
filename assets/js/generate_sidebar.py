import json
import os
from datetime import datetime, timedelta
from threading import Thread
import time

# Iterate over the dataframe rows and schedule jobs initially
list_of_pages = ["base64", "csv2xml", "hex", "index", "json", "json2yaml", "url", "xml", "xml2json", "yaml"]
txt = '<nav id="sidebar"> <div class="sidebar-header"> <a href="index.html" class="h1">&lt;/&gt;</a> </div> <ul class="list-unstyled components"> <li> <a href="#encodeDecode" data-toggle="collapse" aria-expanded="true" class="dropdown-toggle">Encoders & Decoders</a> <ul class="list-unstyled" id="encodeDecode"> <li> <a href="base64.html">Base64</a> </li> <li> <a href="hex.html">Hex</a> </li> <li> <a href="url.html">Url</a> </li> </ul> </li> <!-- <li> <a href="#">About</a> </li> --> <li> <a href="#fomatter" data-toggle="collapse" aria-expanded="true" class="dropdown-toggle">Formatter & Validator</a> <ul class="list-unstyled" id="fomatter"> <li> <a href="json.html">JSON</a> </li> <li> <a href="yaml.html">YAML</a> </li> <li> <a href="xml.html">XML</a> </li> </ul> </li> <li> <a href="#converter" data-toggle="collapse" aria-expanded="true" class="dropdown-toggle">Converters</a> <ul class="list-unstyled" id="converter"> <li> <a href="xml2json.html">XML - JSON</a> </li> <li> <a href="json2yaml.html">JSON - YAML</a> </li> <li> <a href="csv2xml.html">CSV - XML</a> </li> </ul> </li> </nav>'
for page in list_of_pages:
    with open(page+'.template', 'r') as file:
        data = file.read().replace('<div id="sidebar">', '<div id="sidebar">'+txt)
    posts_file = open("../../"+page+".html", "wb")
    posts_file.write(data.encode('utf8'))
    posts_file.close()