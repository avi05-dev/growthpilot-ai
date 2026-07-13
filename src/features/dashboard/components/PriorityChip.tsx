import { Chip } from '@mui/material';

import { priorityColors, type Priority } from '../../../theme/tokens';

type PriorityChipProps = {
  priority: Priority;
};

export function PriorityChip({ priority }: PriorityChipProps) {
  return <Chip size="small" color={priorityColors[priority]} variant="outlined" label={priority} />;
}
