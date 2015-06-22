
# ./test.sh nginx nginx_access nginx_access.log

sudo mkdir -p /opt/logstash/patterns
sudo chown logstash:logstash /opt/logstash/patterns
sudo cp ../files/logstash-patterns /opt/logstash/patterns

cp $3 test.log

cat > test.conf << EOL
input {

  stdin {
    type => "$2"
  }

}
EOL

cat ../templates/logstash_$1_filter.conf >> test.conf

cat test.log | /opt/logstash/bin/logstash agent -e "`cat test.conf`"

