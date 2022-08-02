import React from 'react';

const Total = (props) => {
    console.log(props)
    return (
        <div className={'total'}>
            <h1>Total, $</h1>
            <p>{props.total}</p>
        </div>
    );
};

export default Total;