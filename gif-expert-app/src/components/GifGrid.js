import React, { useState, useEffect } from 'react';
import { getGifs } from '../helpers/GetGifs';
import { GifGridItems } from './GifGridItems';

export const GifGrid = ({ category }) => {

   const [images, setImages] = useState([])

   // Ejecutar la petición Fetch solo una vez
   useEffect(() => {
      getGifs(category).then(imgs => setImages(imgs))
   }, [category])


   return (
      <>
         <div className='title'>
            <h3 >{category}</h3>
         </div>

         <div className='card-grid'>

            {
               images.map(imag => (
                  <GifGridItems
                     key={imag.id}
                     {...imag}
                  />
               ))
            }
         </div>
      </>
   )
}
