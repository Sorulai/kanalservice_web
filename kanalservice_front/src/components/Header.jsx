import React from 'react';


const logo = require('../img/logo.png')
const Header = () => {
    return (
        <div className={'header'}>
            <img src={logo} alt="logo"/>
        </div>
    );
};

export default Header;