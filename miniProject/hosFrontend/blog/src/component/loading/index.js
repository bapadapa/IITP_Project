import { Link } from "react-router-dom";
import Main2 from "../main2";
const loading = () => {
  const { city, county } = useParams([]);
  return (
    <a href={`"http://localhost:3000/info/${city}/${county}"`}>Go info </a>
  );
};
export default loading;
