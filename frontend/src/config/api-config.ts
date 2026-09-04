const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

export const API_ENDPOINTS = {
    
  health: `${API_BASE_URL}/health`

} as const;

export default API_BASE_URL;