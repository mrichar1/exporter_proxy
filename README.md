# exporter_proxy

A small pure-python Reverse HTTP proxy for Prometheus exporters with TLS support.

# Installation

`exporter_proxy` can be downloaded and run as a standalone script. `setup.py` is provided for simplifying package builds.

# Use

```
exporter_proxy --help
usage: exporter_proxy [-h] [-c CONFIG]

Command-line options

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Path to config file. (Defaults to: /etc/prometheus/exporter_proxy.ini)
```

# Configuration

The configuration is held in an `ini-file`. The section title must be `[exporter_proxy]`. See `config.ini` as an example.

The following configuration options are available:

* _proxy_address_ - The address to bind the proxy listener to.
* _proxy_port_ - The port to bind the proxy listener to.
* _server_url_ - The URL (optionally including port) of the server to proxy.
* _ssl_cert_ - Path to file containing the public certificate or chain for the proxy server (optional - if set enables SSL).
* _ssl_key_ - Path to file containing the certificate key for the proxy server. (optional, if key is in the certfile).
* _ssl_verify_ - Should client certificate verification be performed. (optional).

## Prometheus

The documentation on configuring Prometheus to scrape using TLS is here: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#tls_config

TLS is configured separately for each scrape job:

```
scrape_configs:
  - job_name: node
    scheme: https
    tls_config:
        cert_file: /etc/prometheus/exporter_proxy.crt
        key_file: /etc/prometheus/exporter_proxy.key
    file_sd_configs:
    - files:
      - /etc/prometheus/targets.d/node_targets.json
```
