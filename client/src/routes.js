import App from "./App";
import Home from "./components/Home";
import Cars from "./components/Cars";
import About from "./components/About";
import CarsDetail from "./components/CarsDetails";
import ErrorPage from "./components/ErrorPage";

const routes = [
    {
        path: '/',
        element: <App />,
        errorElement: <ErrorPage />,
        children: [
            {
                path: '/',
                element: <Home />
            }, 
            {
                path: '/cars',
                element: <Cars />,
                
            },
            {
                path: '/cars-detail/:id',
                element: <CarsDetail />
            },  
            {
                path: '/about',
                element: <About />
            }, 
        ]    
    }
]

export default routes;