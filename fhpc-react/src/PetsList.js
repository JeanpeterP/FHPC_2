import { useEffect, useState } from "react";
import Config from "./utils/config"

export default function PetsList(){
    const [pets, setPets] = useState([]);

    const getData = async () => {
        const response_pets = await fetch(Config.petsUrl);

        if (response_pets.ok) {
            const data_pets = await response_pets.json();
            console.log(data_pets)
            setPets(data_pets)
        }
    }

    useEffect(() => {
        getData();
    }, []);

    return (
        <div>
            <table className="table table-striped">
            <thead>
                <tr>
                <th>Name</th>
                <th>Breed</th>
                <th>Weight</th>
                </tr>
            </thead>
            <tbody>
                {pets.map(pet => {
                    return (
                    <tr>
                        <td>{pet.name}</td>
                        <td>{pet.breed}</td>
                    </tr>
                    )
                })}
            </tbody>
            </table>
        </div>
      );
}