--
-- rkwapQL database dump
--

-- Dumped from database version 12.4
-- Dumped by pg_dump version 12.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: android; Type: SCHEMA; Schema: -; Owner: rkwap
--

CREATE SCHEMA android;


ALTER SCHEMA android OWNER TO rkwap;

--
-- Name: SCHEMA android; Type: COMMENT; Schema: -; Owner: rkwap
--

COMMENT ON SCHEMA android IS 'for android users';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: bugs; Type: TABLE; Schema: android; Owner: rkwap
--

CREATE TABLE android.bugs (
    id bigint NOT NULL,
    feed_id bigint NOT NULL,
    app_id character varying(255) NOT NULL
);


ALTER TABLE android.bugs OWNER TO rkwap;

--
-- Name: bugs_id_seq; Type: SEQUENCE; Schema: android; Owner: rkwap
--

CREATE SEQUENCE android.bugs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE android.bugs_id_seq OWNER TO rkwap;

--
-- Name: bugs_id_seq; Type: SEQUENCE OWNED BY; Schema: android; Owner: rkwap
--

ALTER SEQUENCE android.bugs_id_seq OWNED BY android.bugs.id;


--
-- Name: devs; Type: TABLE; Schema: android; Owner: rkwap
--

CREATE TABLE android.devs (
    user_id bigint NOT NULL,
    app_id character varying(255) NOT NULL
);


ALTER TABLE android.devs OWNER TO rkwap;

--
-- Name: discovery; Type: TABLE; Schema: android; Owner: rkwap
--

CREATE TABLE android.discovery (
    id bigint NOT NULL,
    feed_id bigint NOT NULL,
    app_id character varying NOT NULL
);


ALTER TABLE android.discovery OWNER TO rkwap;

--
-- Name: discovery_id_seq; Type: SEQUENCE; Schema: android; Owner: rkwap
--

CREATE SEQUENCE android.discovery_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE android.discovery_id_seq OWNER TO rkwap;

--
-- Name: discovery_id_seq; Type: SEQUENCE OWNED BY; Schema: android; Owner: rkwap
--

ALTER SEQUENCE android.discovery_id_seq OWNED BY android.discovery.id;


--
-- Name: features; Type: TABLE; Schema: android; Owner: rkwap
--

CREATE TABLE android.features (
    id bigint NOT NULL,
    feed_id bigint NOT NULL,
    app_id character varying NOT NULL
);


ALTER TABLE android.features OWNER TO rkwap;

--
-- Name: features_id_seq; Type: SEQUENCE; Schema: android; Owner: rkwap
--

CREATE SEQUENCE android.features_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE android.features_id_seq OWNER TO rkwap;

--
-- Name: features_id_seq; Type: SEQUENCE OWNED BY; Schema: android; Owner: rkwap
--

ALTER SEQUENCE android.features_id_seq OWNED BY android.features.id;


--
-- Name: feeds; Type: TABLE; Schema: android; Owner: rkwap
--

CREATE TABLE android.feeds (
    id bigint NOT NULL,
    title character varying(255) NOT NULL,
    body text NOT NULL,
    sub character(2) NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone,
    upvote character varying(255),
    downvote character varying(255),
    tag1 character varying(100) NOT NULL,
    tag2 character varying(100),
    tag3 character varying(100),
    app_id character varying(255) NOT NULL,
    user_id bigint,
    dev_body character varying(300)
);


ALTER TABLE android.feeds OWNER TO rkwap;

--
-- Name: feeds_id_seq; Type: SEQUENCE; Schema: android; Owner: rkwap
--

CREATE SEQUENCE android.feeds_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE android.feeds_id_seq OWNER TO rkwap;

--
-- Name: feeds_id_seq; Type: SEQUENCE OWNED BY; Schema: android; Owner: rkwap
--

ALTER SEQUENCE android.feeds_id_seq OWNED BY android.feeds.id;


--
-- Name: new_release; Type: TABLE; Schema: android; Owner: rkwap
--

CREATE TABLE android.new_release (
    id bigint NOT NULL,
    feed_id bigint NOT NULL,
    app_id character varying NOT NULL
);


ALTER TABLE android.new_release OWNER TO rkwap;

--
-- Name: new_release_id_seq; Type: SEQUENCE; Schema: android; Owner: rkwap
--

CREATE SEQUENCE android.new_release_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE android.new_release_id_seq OWNER TO rkwap;

--
-- Name: new_release_id_seq; Type: SEQUENCE OWNED BY; Schema: android; Owner: rkwap
--

ALTER SEQUENCE android.new_release_id_seq OWNED BY android.new_release.id;


--
-- Name: price_drop; Type: TABLE; Schema: android; Owner: rkwap
--

CREATE TABLE android.price_drop (
    id bigint NOT NULL,
    feed_id bigint NOT NULL,
    app_id character varying NOT NULL
);


ALTER TABLE android.price_drop OWNER TO rkwap;

--
-- Name: price_drop_id_seq; Type: SEQUENCE; Schema: android; Owner: rkwap
--

CREATE SEQUENCE android.price_drop_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE android.price_drop_id_seq OWNER TO rkwap;

--
-- Name: price_drop_id_seq; Type: SEQUENCE OWNED BY; Schema: android; Owner: rkwap
--

ALTER SEQUENCE android.price_drop_id_seq OWNED BY android.price_drop.id;


--
-- Name: spotlight; Type: TABLE; Schema: android; Owner: rkwap
--

CREATE TABLE android.spotlight (
    id bigint NOT NULL,
    feed_id bigint NOT NULL,
    app_id character varying NOT NULL
);


ALTER TABLE android.spotlight OWNER TO rkwap;

--
-- Name: spotlight_id_seq; Type: SEQUENCE; Schema: android; Owner: rkwap
--

CREATE SEQUENCE android.spotlight_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE android.spotlight_id_seq OWNER TO rkwap;

--
-- Name: spotlight_id_seq; Type: SEQUENCE OWNED BY; Schema: android; Owner: rkwap
--

ALTER SEQUENCE android.spotlight_id_seq OWNED BY android.spotlight.id;


--
-- Name: update; Type: TABLE; Schema: android; Owner: rkwap
--

CREATE TABLE android.update (
    id bigint NOT NULL,
    feed_id bigint NOT NULL,
    app_id character varying NOT NULL
);


ALTER TABLE android.update OWNER TO rkwap;

--
-- Name: update_id_seq; Type: SEQUENCE; Schema: android; Owner: rkwap
--

CREATE SEQUENCE android.update_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE android.update_id_seq OWNER TO rkwap;

--
-- Name: update_id_seq; Type: SEQUENCE OWNED BY; Schema: android; Owner: rkwap
--

ALTER SEQUENCE android.update_id_seq OWNED BY android.update.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: rkwap
--

CREATE TABLE public.users (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    username character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    password character varying(255) NOT NULL,
    profile_pic text,
    reputation character varying,
    date_joined timestamp with time zone NOT NULL,
    last_login timestamp with time zone,
    about character varying(255),
    is_dev boolean,
    is_admin boolean,
    is_mod boolean
);


ALTER TABLE public.users OWNER TO rkwap;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: rkwap
--

CREATE SEQUENCE public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO rkwap;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rkwap
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: bugs id; Type: DEFAULT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.bugs ALTER COLUMN id SET DEFAULT nextval('android.bugs_id_seq'::regclass);


--
-- Name: discovery id; Type: DEFAULT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.discovery ALTER COLUMN id SET DEFAULT nextval('android.discovery_id_seq'::regclass);


--
-- Name: features id; Type: DEFAULT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.features ALTER COLUMN id SET DEFAULT nextval('android.features_id_seq'::regclass);


--
-- Name: feeds id; Type: DEFAULT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.feeds ALTER COLUMN id SET DEFAULT nextval('android.feeds_id_seq'::regclass);


--
-- Name: new_release id; Type: DEFAULT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.new_release ALTER COLUMN id SET DEFAULT nextval('android.new_release_id_seq'::regclass);


--
-- Name: price_drop id; Type: DEFAULT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.price_drop ALTER COLUMN id SET DEFAULT nextval('android.price_drop_id_seq'::regclass);


--
-- Name: spotlight id; Type: DEFAULT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.spotlight ALTER COLUMN id SET DEFAULT nextval('android.spotlight_id_seq'::regclass);


--
-- Name: update id; Type: DEFAULT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.update ALTER COLUMN id SET DEFAULT nextval('android.update_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: rkwap
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: bugs bugs_pkey; Type: CONSTRAINT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.bugs
    ADD CONSTRAINT bugs_pkey PRIMARY KEY (id);


--
-- Name: discovery discovery_pkey; Type: CONSTRAINT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.discovery
    ADD CONSTRAINT discovery_pkey PRIMARY KEY (id);


--
-- Name: features features_pkey; Type: CONSTRAINT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.features
    ADD CONSTRAINT features_pkey PRIMARY KEY (id);


--
-- Name: feeds feeds_pkey; Type: CONSTRAINT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.feeds
    ADD CONSTRAINT feeds_pkey PRIMARY KEY (id);


--
-- Name: new_release new_release_pkey; Type: CONSTRAINT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.new_release
    ADD CONSTRAINT new_release_pkey PRIMARY KEY (id);


--
-- Name: devs pk; Type: CONSTRAINT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.devs
    ADD CONSTRAINT pk PRIMARY KEY (user_id, app_id);


--
-- Name: price_drop price_drop_pkey; Type: CONSTRAINT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.price_drop
    ADD CONSTRAINT price_drop_pkey PRIMARY KEY (id);


--
-- Name: spotlight spotlight_pkey; Type: CONSTRAINT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.spotlight
    ADD CONSTRAINT spotlight_pkey PRIMARY KEY (id);


--
-- Name: update update_pkey; Type: CONSTRAINT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.update
    ADD CONSTRAINT update_pkey PRIMARY KEY (id);


--
-- Name: users email; Type: CONSTRAINT; Schema: public; Owner: rkwap
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT email UNIQUE (email);


--
-- Name: users username; Type: CONSTRAINT; Schema: public; Owner: rkwap
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT username UNIQUE (username);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: rkwap
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: fki_feeds_fkey; Type: INDEX; Schema: android; Owner: rkwap
--

CREATE INDEX fki_feeds_fkey ON android.feeds USING btree (user_id);


--
-- Name: fki_fk; Type: INDEX; Schema: android; Owner: rkwap
--

CREATE INDEX fki_fk ON android.devs USING btree (user_id);


--
-- Name: devs devs_fkey; Type: FK CONSTRAINT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.devs
    ADD CONSTRAINT devs_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: feeds feeds_fkey; Type: FK CONSTRAINT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.feeds
    ADD CONSTRAINT feeds_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) MATCH FULL ON UPDATE SET NULL ON DELETE SET NULL NOT VALID;


--
-- Name: bugs fk; Type: FK CONSTRAINT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.bugs
    ADD CONSTRAINT fk FOREIGN KEY (feed_id) REFERENCES android.feeds(id) MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: features fk; Type: FK CONSTRAINT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.features
    ADD CONSTRAINT fk FOREIGN KEY (feed_id) REFERENCES android.feeds(id) MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: new_release fk; Type: FK CONSTRAINT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.new_release
    ADD CONSTRAINT fk FOREIGN KEY (feed_id) REFERENCES android.feeds(id) MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: spotlight fk; Type: FK CONSTRAINT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.spotlight
    ADD CONSTRAINT fk FOREIGN KEY (feed_id) REFERENCES android.feeds(id) MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: price_drop fk; Type: FK CONSTRAINT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.price_drop
    ADD CONSTRAINT fk FOREIGN KEY (feed_id) REFERENCES android.feeds(id) MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: discovery fk; Type: FK CONSTRAINT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.discovery
    ADD CONSTRAINT fk FOREIGN KEY (feed_id) REFERENCES android.feeds(id) MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: update fk; Type: FK CONSTRAINT; Schema: android; Owner: rkwap
--

ALTER TABLE ONLY android.update
    ADD CONSTRAINT fk FOREIGN KEY (feed_id) REFERENCES android.feeds(id) MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- rkwapQL database dump complete
--

