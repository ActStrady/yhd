drop database if exists yhd;
create database yhd;

drop table if exists yhd.iphone;
create table yhd.iphone(
    id int primary key auto_increment comment '主键',
    name varchar(255) comment '名称',
    price varchar(255) comment '价格',
    praise varchar(255) comment '好评率',
    store_name varchar(255) comment '店铺名',
    image_url varchar(255) comment '图片地址'
) comment 'iphone信息';

# 删除表所有内容
truncate yhd.iphone;