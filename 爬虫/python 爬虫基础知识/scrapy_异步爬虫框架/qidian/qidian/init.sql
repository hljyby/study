create table t_book(
    book_id varchar(32) primary key,
    `name` varchar(100),
    cover varchar(200),
    summary text,
    `url` varchar(50),
    author varchar(50),
    tags varchar(50)
);

create table t_seg(
    seg_id varchar(32) primary key,
    book_id varchar(32),
    title varchar(50),
    seg_url varchar(50)
);

create table t_detail_seg(
    seg_id varchar(32),
    `text` text
);