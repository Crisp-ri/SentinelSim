# System Architecture

---

## Overview

---

The simulator generates controlled test traffic and synthetic events that imitate real attack patterns.

In traffic mode, the simulator produces real HTTP requests against local services to generate authentic system logs.

It consists of six independent modules:

- Attack Simulator

- API Layer

- Log ingestion Layer

- Detection Engine

- Storage Layer

- Frontend Dashboard

The architecture follows a modular pipeline design, where each component performs a specific responsibility.

---

# Core Components

---

## Attack Simulator

---

The simulator generates synthetic security events that imitate real attack patterns.

Supported scenarios:

- Brute force login attempts

- Port scanning activity

- DDoS-like request spikes

- Suspicious payload patterns (e.g., SQL injection strings)

The simulator does not analyze or store events. It only produces event streams.

---

## API Layer (FastAPI)

---

The API serves as the entry point for all event data.

Responsibilities:

- Accept incoming events from simulator or external sources

- Validate event structure

- Forward events to the Detection Engine

- Provide data access for frontend dashboards

---

## Log Ingestion Layer

---

The Log Ingestion Layer is responsible for collecting and processing raw logs from local services.

It supports:

- FastAPI access logs

- Web server logs

- External log files

The layer converts unstructured log entries into normalized event objects that can be processed by the Detection Engine.
This component enables analysis of real system activity while keeping all attack scenarios safe and limited to the local environment.

---

## Detection Engine

---

The Detection Engine processes incoming events in real time.

It applies multiple detection algorithms:

- Brute force detection using sliding time windows

- Port scan detection using IP-port set analysis

- Traffic spike detection using statistical z-score analysis

- Suspicious payload pattern matching

The engine calculates a suspicious score for each IP address and generates alerts.

---

## Storage Layer

---

Data is stored using SQLite and SQLAlchemy ORM.

The database stores:

- Raw events

- Generated alerts

- Aggregated statistics per IP address

The storage layer is independent from detection logic.

---

## Frontend Dashboard

---

The frontend is built with React and provides:

- Real-time event visualization

- Alert monitoring

- IP statistics overview

- Attack simulation controls

---

# Event Processing Pipeline

---

Traffic Generator / External Logs → Log Parser → Detection Engine → Database → Dashboard

---

## Data Sources

- Attack Simulator

- External log files

- Direct API input

---

# Design Principles

- Modular architecture

- Separation of concerns

- Real-time processing capability

- Extensibility for additional detectors
