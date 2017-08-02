---
layout: default
---

<div class="row">
  <div class="col-md-12 text-center">
    <div class="jumbotron">
      <h1>Sharing threat intelligence just got a lot easier!</h1>
    </div>
  </div>

  <div class="col-md-6">
    <div class="panel panel-default">
      <div class="panel-heading">
        <div markdown="span">![STIX Logo]({{ site.baseurl }}/img/stix.png){: .panel-logo}</div>
        <div class="panel-title text-center">A structured language for cyber threat intelligence</div>
        <a class="btn btn-primary btn-spec" data-toggle="tooltip" title="STIX Committee Specification" href="https://docs.google.com/document/d/1yvqWaPPnPW-2NiVCLqzRszcx91ffMowfT5MmE9Nsy_w">
          <span class="glyphicon glyphicon-list-alt"></span> Read the Latest Specification
        </a>
        </div>          
      <div class="panel-body">
        <p>
          Structured Threat Information Expression (STIX™) is a language and serialization format used to exchange cyber threat intelligence (CTI).
        </p>
        <p>
          STIX enables organizations to share CTI with one another in a consistent and machine readable manner, allowing security communities to better understand what computer-based attacks they are most likely to see and to anticipate and/or respond to those attacks faster and more effectively.
        </p>
        <p>
          STIX is designed to improve many different capabilities, such as collaborative threat analysis, automated threat exchange, automated detection and response, and more.
        </p>

        <div class="figure text-center" markdown="span">
        ![STIX 2.0 Relationship Example]({{ site.baseurl }}/img/stix2_relationship_example_2.png){: .figure-img .img-fluid}
        **STIX 2.0 Relationship Example**
        </div>
      </div>
    </div>
  </div>

  <div class="col-md-6">
    <div class="panel panel-default">
      <div class="panel-heading">
        <div markdown="span">![TAXII Logo]({{ site.baseurl }}/img/taxii.png){: .panel-logo}</div>
        <div class="panel-title text-center">A transport mechanism for sharing cyber threat intelligence</div>
        <a class="btn btn-primary btn-spec" data-toggle="tooltip" title="TAXII Committee Specification" href="https://docs.google.com/document/d/1eyhS3-fOlRkDB6N39Md6KZbvbCe3CjQlampiZPg-5u4">
          <span class="glyphicon glyphicon-list-alt"></span> Read the Latest Specification (Draft 2)
        </a>
      </div>
      <div class="panel-body">
        <p>
          Trusted Automated Exchange of Intelligence Information (TAXII™) is an application layer protocol for the communication of cyber threat information in a simple and scalable manner.
        <p>
        </p>
          TAXII is a protocol used to exchange cyber threat intelligence (CTI) over HTTPS. TAXII enables organizations to share CTI by defining an API that aligns with common sharing models.
        <p>
        </p>
          TAXII is specifically designed to support the exchange of CTI represented in STIX.
        </p>
        <p>
        <div class="figure center-block text-center" markdown="span">
          ![TAXII Collections and Channels]({{ site.baseurl }}/img/taxii_diagram.png){: .figure-img .img-fluid}
          **TAXII Collections and Channels**
        </div>
        </p>
      </div>
    </div>
  </div>
</div>
