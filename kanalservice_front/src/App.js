import React, {useState} from "react";
import Header from "./components/Header";
import axios from "axios";
import './style/App.css'
import Total from "./components/Total";


function App() {
    const [data, setData] = useState()

    async function fetchData() {
        const response = await axios.get('http://localhost:1337/api/v1/list-orders/')
        setData(response.data)


    }

    return (
        <div className="App">
            <Header/>
             <button onClick={fetchData} className={'btn'}>Загрузить данные</button>
            <div className={'wrapper'}>
                <table className={'table'}>
                    <caption>Данные из Google sheets</caption>
                    <tr className={'table-header'}>
                        <th>№</th>
                        <th>№ заказа</th>
                        <th>Стоимость,$</th>
                        <th>Стоимость,руб</th>
                        <th>Срок поставки</th>
                    </tr>
                    {data && data.orders.map((item) => {
                        return (
                            <tr className={'table-item'}>
                                <td>{item.order_id}</td>
                                <td>{item.order_number}</td>
                                <td>{item.order_cost_usd}</td>
                                <td>{item.order_cost_rub}</td>
                                <td>{item.delivery_date}</td>

                            </tr>
                        )
                    })}
                </table>
                <Total total={data && data.total_usd}/>

            </div>

        </div>
    );
}

export default App;
