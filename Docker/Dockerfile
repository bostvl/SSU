FROM centos7/hw 
MAINTAINER my <bsv@localhost>
#RUN yum update -y
RUN yum install -y httpd
#RUN systemctl enable httpd
RUN echo "Homework6!">/var/www/html/index.html
EXPOSE 80
CMD /usr/sbin/httpd -D FOREGROUND
