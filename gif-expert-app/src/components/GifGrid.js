import React, { useState, useEffect } from 'react';
import { GifGridItems } from './GifGridItems';

export const GifGrid = ({ category }) => {

   const [images, setImages] = useState([])

   // Ejecutar la petición Fetch solo una vez
   useEffect(() => {
      getGifs();
   }, [])

   const getGifs = async () => {
      const url = `https://api.giphy.com/v1/gifs/search?q=${encodeURI( category )}&limit=10&api_key=pOFtYHGzH718DYtBKguubBLqSqEdL6IS`;
      const resp = await fetch(url);
      const { data } = await resp.json();

      const gifs = data.map(img => {
         return {
            id: img.id,
            title: img.title,
            url: img.images?.downsized_medium.url
         }
      })

      console.log(gifs);
      setImages(gifs)
   }
   /* getGifs(); */

   return (
      <>
         <h3>{category}</h3>
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
