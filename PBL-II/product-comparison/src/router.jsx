import { createBrowserRouter } from 'react-router-dom'
import Home from './screens/Home'
import ElectronicsSearch from './screens/Electronics'
import FashionSearch from './screens/Fashion';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Home />
  },
  {
    path: '/electronics',
    element: <ElectronicsSearch />
  },
  {
    path: '/fashion',
    element: <FashionSearch />
  }
]);

export default router