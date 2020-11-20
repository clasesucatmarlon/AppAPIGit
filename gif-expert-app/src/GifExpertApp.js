import React, { useState } from 'react';
import { AddCategory } from './components/AddCategory';
import { GifGrid } from './components/GifGrid';

const GifExpertApp = () => {

    const [categories, setCategories] = useState(['One Punh'])

    /*     //AGREGAR NUEVO ELEMENTO AL ARRAY
        const handleAdd = () => {
            setCategories([...categories, 'Hola'])
        } */



    return (
        <>
            <h2>GifExpertApp</h2>
            <AddCategory setCateg={setCategories} />
            <hr />

            {/* <button onClick={handleAdd}>Agregar</button> */}
            <ol>
                {
                    categories.map((category) => (
                        <GifGrid
                            key={ category }
                            category={category} />
                    ))
                }
            </ol>
        </>
    )
}

export default GifExpertApp;
