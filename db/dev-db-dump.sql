--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

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
-- Name: settings_type; Type: TYPE; Schema: public; Owner: flask_user
--

CREATE TYPE public.settings_type AS ENUM (
    'LINKEDIN_BIO',
    'TOTAL_EXPERIENCE',
    'CURRENT_EXPERIENCE',
    'LIST_OF_PAST_JOBS',
    'CURRENT_JOB_DESCRIPTION',
    'CURRENT_JOB_SPECIALTIES'
);


ALTER TYPE public.settings_type OWNER TO flask_user;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: personalization_settings; Type: TABLE; Schema: public; Owner: flask_user
--

CREATE TABLE public.personalization_settings (
    id integer NOT NULL,
    created_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    user_id integer,
    is_disabled boolean NOT NULL,
    name public.settings_type NOT NULL,
    description character varying(255) NOT NULL,
    value boolean NOT NULL
);


ALTER TABLE public.personalization_settings OWNER TO flask_user;

--
-- Name: personalization_settings_id_seq; Type: SEQUENCE; Schema: public; Owner: flask_user
--

CREATE SEQUENCE public.personalization_settings_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.personalization_settings_id_seq OWNER TO flask_user;

--
-- Name: personalization_settings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: flask_user
--

ALTER SEQUENCE public.personalization_settings_id_seq OWNED BY public.personalization_settings.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: flask_user
--

CREATE TABLE public.users (
    id integer NOT NULL,
    created_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modified_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    is_active boolean NOT NULL,
    email character varying(64) NOT NULL,
    first_name character varying(255),
    last_name character varying(255),
    password character varying(255)
);


ALTER TABLE public.users OWNER TO flask_user;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: flask_user
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO flask_user;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: flask_user
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: personalization_settings id; Type: DEFAULT; Schema: public; Owner: flask_user
--

ALTER TABLE ONLY public.personalization_settings ALTER COLUMN id SET DEFAULT nextval('public.personalization_settings_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: flask_user
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: personalization_settings; Type: TABLE DATA; Schema: public; Owner: flask_user
--

COPY public.personalization_settings (id, created_date, modified_date, user_id, is_disabled, name, description, value) FROM stdin;
1	2023-12-03 20:47:59.402789	2023-12-03 20:47:59.402789	1	f	LINKEDIN_BIO	Enable LinkedIn Bio	t
2	2023-12-03 20:47:59.402789	2023-12-03 20:47:59.402789	1	f	TOTAL_EXPERIENCE	Year of Experience	t
3	2023-12-03 20:47:59.402789	2023-12-03 20:47:59.402789	1	f	CURRENT_EXPERIENCE	Current Experience	t
4	2023-12-03 20:47:59.402789	2023-12-03 20:47:59.402789	1	f	LIST_OF_PAST_JOBS	List of Past Jobs	f
5	2023-12-03 20:47:59.402789	2023-12-03 20:47:59.402789	1	t	CURRENT_JOB_DESCRIPTION	Current Job Description	f
6	2023-12-03 20:47:59.402789	2023-12-03 20:47:59.402789	1	t	CURRENT_JOB_SPECIALTIES	Current Job Specialties	f
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: flask_user
--

COPY public.users (id, created_date, modified_date, is_active, email, first_name, last_name, password) FROM stdin;
1	2023-12-03 20:47:59.402789	2023-12-03 20:47:59.402789	t	arslan@example.com	Muhammad	Arslan	$2b$12$SErZz.S8y71vTFOuNWak.ect7TybldVTZ7uET2nxZ93o.dOgAqzvq
\.


--
-- Name: personalization_settings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: flask_user
--

SELECT pg_catalog.setval('public.personalization_settings_id_seq', 6, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: flask_user
--

SELECT pg_catalog.setval('public.users_id_seq', 1, true);


--
-- Name: personalization_settings personalization_settings_pkey; Type: CONSTRAINT; Schema: public; Owner: flask_user
--

ALTER TABLE ONLY public.personalization_settings
    ADD CONSTRAINT personalization_settings_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: flask_user
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: personalization_settings personalization_settings_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: flask_user
--

ALTER TABLE ONLY public.personalization_settings
    ADD CONSTRAINT personalization_settings_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

