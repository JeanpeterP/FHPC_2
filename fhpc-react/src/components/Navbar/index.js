import React from 'react'
import {FaBars} from 'react-icons/fa'
import {
    Nav,
    NavbarContainer,
    NavLogo,
    MobileIcon,
    NavMenu,
    NavItem,
    NavLinks,
    NavBtn,
    NavBtnLink
} from './NavbarElements';

const Navbar = ({ isLoggedIn, handleLogout }) => {
    return (
      <>
        <Nav>
          <NavbarContainer>
            <NavLogo to="/">Dollarrr</NavLogo>
            <MobileIcon>
              <FaBars />
            </MobileIcon>
            <NavMenu>
              <NavItem>
                <NavLinks to="about">About</NavLinks>
              </NavItem>
              <NavItem>
                <NavLinks to="services">Services</NavLinks>
              </NavItem>
              <NavItem>
                <NavLinks to="signup">Sign Up</NavLinks>
              </NavItem>
              {isLoggedIn ? (
                <NavItem>
                  <NavLinks to="/" onClick={handleLogout}>
                    Logout
                  </NavLinks>
                </NavItem>
              ) : (
                <NavItem>
                  <NavLinks to="/login">Login</NavLinks>
                </NavItem>
              )}
            </NavMenu>
          </NavbarContainer>
          <NavBtn>
                <NavBtnLink to="/signin">Sign In</NavBtnLink>
          </NavBtn>
        </Nav>
      </>
    );
  };

export default Navbar