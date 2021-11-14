**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation
*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

- All pods and service in **default** namespace
    ![all-pod-svc-default](.\answer-img\all-pod-svc-default.png)
- All pods and service in **monitoring** namespace
    ![all-pod-svc-monitoring](.\answer-img\all-pod-svc-monitoring.png)
- All pods and service in **observability** namespace
    ![all-pod-svc-observability](.\answer-img\all-pod-svc-observability.png)

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

```bash
 kubectl port-forward -n monitoring prometheus-grafana-5cddc775c4-65px7 3000
```

**Grafana Homepage**
![grafana-homepage.png](.\answer-img\grafana-homepage.png)

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

**Grafana with Prometheus as data source**
![grafana-basic-prom.png](.\answer-img\grafana-basic-prom.png)

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

- **Service Level Objectives** - SLO is a measurable goal set by the DRE team to ensure a standard level of performance during a specific period of time. SLOs are the targeted levels of service, measured by SLIs. They are typically expressed as in a percentage over a time period. example: 95% of all HTTP requests to an particular end-point should be < 10 milliseconds.

- **Service Level Indicators** - SLI is a specific metric used to measure the performance of a service. SLIs are the metrics used to measure the level of service provided to end users (e.g., availability, latency, throughput). e.g. The percentage rate at which HTTP requests are failing.

**SLIs for monthly uptime SLA:** If an SLA specifies that the service/systems monthly uptime or availability will be available 99.98% of the time, the SLO will likely be 99.92% uptime and so the SLI is the real/actual measurement of service/system uptime.

**SLI for request response time SLA:** Request response time is the average response time of a transaction from the perspective of the requester in order for complete the task of the API. If SLA specifies the service/systems for every additional .5% of 500s response (internal server error), 5% refund of total contract will be issued. The SLO will likely be less 2% HTTP 500s over 30 days and the SLI indicator is HTTP status codes

References: [establishing-service-level-objectives](https://www.datadoghq.com/blog/establishing-service-level-objectives/#:~:text=Service%20Level%20Indicators%20(SLIs)%20are,over%20a%20period%20of%20time)

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs.
- **Uptime** - The time which a service is active or the percentage of time the website/web services are available and responding/functioning as expected.
- **Errors** - The count or amount of requests that are failing or erroring out instead a successful response. eg. HTTP 500 _Internal Sever Error_ response.
- **Traffic** - The load or amount of stress on a service/system from its consumers. eg. number of HTTP requests/second.
- **Saturation** - The limit or the overall capacity of a system/service. eg. percentage of memory being used.
- **Latency** - It is the response time for an requests or the time taken to serve a request which are usually measured in ms. It is very important and critical to differentiate between the latency of an failed or successful requests, because it's very critical to track error response time, as it is opposed to just filtering out errors.

The Errors, Traffic, Saturations, and Latency are the metrics which are **Four Golden Signals** for any application/service/system.

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here.

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue.

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name three SLIs that you would use to measure the success of this SLO.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create KPIs to accurately measure these metrics. We will make a dashboard for this, but first write them down here.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
