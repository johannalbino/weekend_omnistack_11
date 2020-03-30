import React, { useEffect, useState } from 'react';
import logo from '../../assets/logo.svg'
import { Link, useHistory } from 'react-router-dom';
import { FiPower, FiTrash2 } from 'react-icons/fi';
import './styles.css';
import api from '../../services/api';

export default function Profile(){

    const [incidents, setIncidents] = useState([]);
    const history = useHistory();

    const tokenOng = localStorage.getItem('token');
    const ongName = localStorage.getItem('ongName');

    useEffect(() => {
        api.get('profile/', {
            headers: {
                Authorization: `token ${tokenOng}`,
            }
        }).then(response => {
            setIncidents(response.data);
        })
    }, [tokenOng]);

    function handleDeleteIncident(id) {
        try{
            api.delete(`incidents/${id}`, {
                headers: {
                    Authorization: `token ${tokenOng}`
                }
            });

            setIncidents(incidents.filter(incident => incident.id_incidents != id));
        } catch (err){
            alert('Erro ao deletar caso, tente novamente.')
        }
    }

    function handleLogout(){
        localStorage.clear();
        history.push('/');
    }

    return (
        <div className="profile-container">
            <header>
                <img src={logo} alt="Be the Hero" />
                <span>Bem vinda, {ongName}</span>

                <Link className="button" to="/incidents/new">Cadastrar novo caso</Link>
                <button type="button" onClick={() => handleLogout()}>
                    <FiPower size={18} color="#E02041" />
                </button>
            </header>
            <h1>Casos cadastrados</h1>

            <ul>
                {
                    incidents.map(incident => (
                        <li key={incident.id_incidents}>
                            <strong>CASO:</strong>
                            <p>{incident.title_incident}</p>

                            <strong>DESCRIÇÃO:</strong>
                            <p>{incident.description_incident}</p>

                            <strong>VALOR</strong>
                            <p>{Intl.NumberFormat('pt-BR', {style: 'currency', currency: 'BRL'}).format(incident.value_incident)}</p>

                            <button type="button" onClick={() => handleDeleteIncident(incident.id_incidents)}>
                                <FiTrash2 size={20} color="#a8a8b3" />
                            </button>
                        </li>
                    ))
                }
            </ul>
        </div>
    )
}