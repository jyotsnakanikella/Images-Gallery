import React from 'react';
import '../css/index.css';
import { Button } from 'react-bootstrap';

const Welcome = () => {
  return (
    <div class="container-fluid bg-dark text-light p-5">
      <div class="container bg-dark p-5">
        <h1 class="display-4">Images Gallery</h1>
        <hr />
        <p>
          This is simple application that retrieves photos using Unsplash API.
          In order to start enter any search term in the input field.
        </p>
        <Button
          href="https://unsplash.com"
          target="_blank"
          class="btn btn-primary"
        >
          Learn more
        </Button>
      </div>
    </div>
  );
};

export default Welcome;
