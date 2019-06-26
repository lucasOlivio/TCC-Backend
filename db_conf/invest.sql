SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';

CREATE TABLE tb_companies (
    id serial PRIMARY KEY,
    company varchar(125)
);

CREATE TABLE tb_symbol_market (
    id_company integer not NULL references tb_companies(ID) ON DELETE CASCADE,
    market varchar(10),
    symbol varchar(10),
    PRIMARY KEY(id_company, market, symbol)
);

INSERT INTO tb_companies (company)
VALUES ('HP inc.'),('JD.com, Inc.'),('LG Display'),('Intel'),('Panasonic'),('Sony'),('Dell Technologies'),('Hitachi'),('Alphabet Inc.'),('Foxconn Technology Group'),('Samsung Electronics'),('Apple inc.'),('Microsoft corporation'),('Alibaba Group'),('IBM'),('Amazon.com, Inc');

INSERT INTO tb_symbol_market (id_company, symbol, market)
VALUES 
((select id from tb_companies where company = 'HP inc.'), 'HQP','NDAQ'),
((select id from tb_companies where company = 'HP inc.'), 'HPQB34','BVMF'),
((select id from tb_companies where company = 'JD.com, Inc.'), 'JD','NDAQ'),
((select id from tb_companies where company = 'LG Display'), 'LPL','NDAQ'),
((select id from tb_companies where company = 'Intel'), 'INTC','NDAQ'),
((select id from tb_companies where company = 'Intel'), 'ITLC34','BVMF'),
((select id from tb_companies where company = 'Panasonic'), 'PCRFY','NDAQ'),
((select id from tb_companies where company = 'Sony'), 'SNE','NDAQ'),
((select id from tb_companies where company = 'Dell Technologies'), 'DELL','NDAQ'),
((select id from tb_companies where company = 'Hitachi'), 'HTHIY','NDAQ'),
((select id from tb_companies where company = 'Alphabet Inc.'), 'GOOGL','BVMF'),
((select id from tb_companies where company = 'Alphabet Inc.'), 'GOGL35','BVMF'),
((select id from tb_companies where company = 'Alphabet Inc.'), 'GOGL34','BVMF'),
((select id from tb_companies where company = 'Foxconn Technology Group'), 'HNHAF','NDAQ'),
((select id from tb_companies where company = 'Samsung Electronics'), 'SSNLF','NDAQ'),
((select id from tb_companies where company = 'Apple inc.'), 'AAPL','NDAQ'),
((select id from tb_companies where company = 'Apple inc.'), 'AAPL34','BVMF'),
((select id from tb_companies where company = 'Microsoft corporation'), 'MSFT','NDAQ'),
((select id from tb_companies where company = 'Microsoft corporation'), 'MSFT34','BVMF'),
((select id from tb_companies where company = 'Alibaba Group'), 'BABA','NDAQ'),
((select id from tb_companies where company = 'IBM'), 'IBM','NDAQ'),
((select id from tb_companies where company = 'Amazon.com, Inc'), 'AMZN','NDAQ'),
((select id from tb_companies where company = 'Amazon.com, Inc'), 'AMZO34','BVMF');

ALTER TABLE tb_companies OWNER TO lucas;

ALTER TABLE tb_symbol_market OWNER TO lucas;