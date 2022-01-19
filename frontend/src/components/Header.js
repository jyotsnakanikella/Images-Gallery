import React from 'react';
import { Navbar, Container } from 'react-bootstrap';
import { ReactComponent as Logo } from '../images/logo.svg';

const navbarStyle = {
  backgroundColor: '#eeeeee',
};

const Header = ({ title }) => {
  // const { title } = props;
  return (
    <Navbar style={navbarStyle} variant="light">
      <Container>
        {/* <Navbar.Brand href="/">{title}</Navbar.Brand> */}
        <Logo alt={title} style={{ maxWidth: '12rem', maxHeight: '2rem' }} />
      </Container>
    </Navbar>
  );
};

export default Header;
