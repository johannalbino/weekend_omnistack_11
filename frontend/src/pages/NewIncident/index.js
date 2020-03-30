import React, { useState } from 'react';
import './styles.css';
import logo from '../../assets/logo.svg';
import { Link, useHistory } from 'react-router-dom';
import { FiArrowLeft } from 'react-icons/fi';
import api from '../../services/api';


export default function NewIncident(){

    const [title_incident, setTitle] = useState('');
    const [description_incident, setDescritpion] = useState('');
    const [value_incident, setValue] = useState('');
    const tokenOng = localStorage.getItem('token');
    const history = useHistory();

    async function handleNewIncident(e){
        e.preventDefault();
        const data = {
            title_incident,
            description_incident,
            value_incident
        }

        try{
            await api.post('profile/', data, {
                headers: {
                    Authorization: `token ${tokenOng}`
                }
            });
            history.push('/profile');
        } catch (err) {
            alert('Erro ao tentar cadastrar');
        }
    }

    return (
        <div className="new-incident-container">
            <div className="content">
                <section>
                    <img src={logo} alt="Be The hero" />

                    <h1>Cadastra novo caso</h1>
                    <p>Descreva o caso detalhadamente para encontrar um herói para resolver isso.</p>
                    
                    <Link className="back-link" to="/profile">
                        <FiArrowLeft size={16} color="#E02041" /> Voltar pra home
                    </Link>
                </section>
                
                <form onSubmit={handleNewIncident}>
                    <input 
                        value={title_incident}
                        onChange={e => setTitle(e.target.value)}
                        placeholder="Titulo do caso" />
                    <textarea 
                        value={description_incident}
                        onChange={e => setDescritpion(e.target.value)}
                        placeholder="Descrição" />
                    <input 
                        value={value_incident}
                        onChange={e => setValue(e.target.value)}
                        placeholder="Valor em reais" />
                    <button className="button" type="submit">Cadastrar</button>
                </form>
            </div>
        </div>
    )
}
