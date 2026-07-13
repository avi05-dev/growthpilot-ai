import CheckCircleOutlineIcon from '@mui/icons-material/CheckCircleOutlined';
import { Box, Stack, Typography } from '@mui/material';

import type { ActionTask } from '../types/dashboard';
import { PriorityChip } from './PriorityChip';

type ActionItemProps = {
  task: ActionTask;
};

export function ActionItem({ task }: ActionItemProps) {
  return (
    <Stack
      component="li"
      direction="row"
      spacing={2}
      sx={{ alignItems: 'flex-start', listStyle: 'none', border: '1px solid', borderColor: 'divider', borderRadius: 3, p: 2 }}
    >
      <Box sx={{ color: 'secondary.main', display: 'grid', placeItems: 'center', pt: 0.25 }}>
        <CheckCircleOutlineIcon fontSize="small" />
      </Box>
      <Box sx={{ minWidth: 0, flexGrow: 1 }}>
        <Stack direction={{ xs: 'column', sm: 'row' }} spacing={1} sx={{ justifyContent: 'space-between', alignItems: { sm: 'center' } }}>
          <Typography sx={{ fontWeight: 800 }}>{task.title}</Typography>
          <PriorityChip priority={task.priority} />
        </Stack>
        <Typography variant="body2" color="text.secondary" sx={{ mt: 0.5 }}>
          {task.description}
        </Typography>
      </Box>
    </Stack>
  );
}
