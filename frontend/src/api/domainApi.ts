import { apiClient } from './client';

export type Domain = {
  id: string;
  name: string;
  display_name: string;
  description: string;
  is_enabled: boolean;
};

export type DomainsResponse = {
  domains: Domain[];
};

export const DomainApi = {
  async getDomains(): Promise<DomainsResponse> {
    const response = await apiClient.get<DomainsResponse>('/api/domains');
    return response.data;
  },
};
