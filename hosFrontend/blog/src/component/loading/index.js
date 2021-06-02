import { Link } from "react-router-dom";
import Main2 from "../main2";
const loading = () => {
  const { city, county } = useParams([]);
  return (
    <div>
      <Main2 city={city} county={county} />
    </div>
  );
};
export default loading;
