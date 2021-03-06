import React, { useState } from 'react';
import { FiLogIn } from 'react-icons/fi';
import './styles.css';
import heroesImg from '../../assets/heroes.png'
import logo from '../../assets/logo.svg'
import { Link, useHistory } from 'react-router-dom';
import api from '../../services/api';

export default function Logon(){

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const history = useHistory();

    async function handleLogin(e){
        e.preventDefault();

        try{
            const response = await api.post('session/', {
                username: username,
                password: password
            });
            localStorage.setItem('token', response.data['token']);

            const responseProfile = await api.get('ong/my_profile/', {
                headers: {
                    Authorization: `token ${response.data['token']}`,
                }
            });
            localStorage.setItem('ongName', responseProfile.data[0]['username']);

            history.push('/profile');
        } catch (err) {
            alert('Falha no login.');
        }
    }
    

    return(
        <div className="logon-container">
            <section className="form">
                <img src={logo} alt="Be The Hero" />

                <form onSubmit={handleLogin}>
                    <h1>Faça seu logon</h1>
                    <input 
                        placeholder="Seu usuário"
                        value={username}
                        onChange={e => setUsername(e.target.value)} />
                    <input
                        placeholder="Sua senha"
                        value={password}
                        type="password"
                        onChange={e => setPassword(e.target.value)} />
                    <button className="button" type="submit">Entrar</button>

                    <Link className="back-link" to="/register">
                        <FiLogIn size={16} color="#E02041" /> Não tenho cadastro!
                    </Link>
                </form>
            </section>
            <img src={heroesImg} alt="Heroes" />
        </div>
    )
}