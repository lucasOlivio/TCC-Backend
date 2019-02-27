--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: players; Type: TABLE; Schema: public; Owner: lucas; Tablespace: 
--

CREATE TABLE players (
    ID integer PRIMARY KEY,
    number integer,
    name varchar(125),
    position varchar(1),
    height numeric,
    weight numeric,
    prior varchar(125),
    draft varchar(20),
    exp numeric,
    sync boolean DEFAULT FALSE
);


ALTER TABLE players OWNER TO lucas;