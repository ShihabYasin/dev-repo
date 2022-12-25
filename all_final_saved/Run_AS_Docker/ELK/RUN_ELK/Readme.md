# Ref:
https://github.com/gnokoheat/elk-with-filebeat-by-docker-compose


## Visit for Kibana
http://localhost:5601/

## Explanation:
1. In "docker-compose.yml": below is for log location to put app log(contains *.log files) (left portion only)
    filebeat:
    ...
      volumes:
      ...
        - /media/yasin/MyStudy/Saved_Downloads/ELK_LOG_DATA_STORAGE:/usr/share/filebeat/mylog

