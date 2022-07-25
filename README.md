<div id="top"></div>
<!--
*** Thanks for checking out the video-library. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue.
*** Don't forget to give the project a star!
*** Thanks again!:D
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">API based video library</h3>

  <p align="center">
    Backend for video storage platfrom.
    <br />
    <a href="https://github.com/shashwat-pd/video_library">View Demo</a>
    ·
    <a href="https://github.com/shashwat-pd/video_library/issues">Report Bug</a>
    ·
    <a href="https://github.com/shashwat-pd/video_library/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


### Built With

* [![Django][Django]]

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Your machine has to have Python installed.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/shashwat-pd/Video_library.git
   ```
2. Activate virtual environment (Optional). </br>
    Make sure you are in the Base Directory.
    ```sh
    cd Video_library
    ```
    ```sh
    pipenv shell
    ```
2. Install Packages
    ```sh
    pipenv install -r requirements.txt
    ```
    OR
     ```sh
    pip install -r requirements.txt
    ```
3. Run Server
   ```sh
   python manage.py runserver
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

API endpoint for the videoApp in the project is available in ` ` route. 

### **_`/api/upload`_**

Type: `POST`

Description: Uploads video in the database after validation.

Requires: video file
Response:

    {
        "message": "validation error message/ Video uploaded successfully"
    }

### **_`/api/videos`_**

Type: `GET`

Description: Lists videos currently in database.

Requires: Nothing

Response:

    {
        "videos": [
            {
                "id":"<id>",
                "file":"<file name>",
                "type":"<video type>",
                "size": "<video size>"
                }
        ]
    }

### **_`/api/videos/<id>`_**

Type: `GET`

Description: Returns a video accoring to the id.

Requires: id
Response:

    {
        "id":"<id>",
        "file":"<file name>",
        "type":"<video type>",
        "size": "<video size>"
     }

### **_`/api/<id>/calculate_cost`_**

Type: `GET`

Description: Returns the cost of video with the id provided.

Requires: id

Response:

    {
        "cost":"<calculated cost>",
    }
    
### **_`/api/being_uploaded`_**

Type: `GET`

Description: Returns the list of files currently being uploaded.

Requires: Nothing

Response:

    {
        "uploading":["file"],
    }



<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Shashwat Poudel - [@linkedin_handle](https://https://www.linkedin.com/in/shashwat-poudel/) 

Project Link: [https://github.com/github_username/repo_name](https://github.com/shashwat-pd/Video_library)

<p align="right">(<a href="#top">back to top</a>)</p>


[Django]: https://img.shields.io/badge/python-django-green
