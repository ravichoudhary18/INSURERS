import { createContext, useState } from "react";

const MainContext = createContext({});

export const MainProvider = ({ children }) => {
  const [isLodaing, setIsLoading] = useState(false)

  return (
    <MainContext.Provider value={{ isLodaing, setIsLoading }}>
      {children}
    </MainContext.Provider>
  );
};

export default MainContext;